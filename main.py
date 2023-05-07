import os
from typing import Optional
from dotenv import load_dotenv  # type: ignore

load_dotenv()
from bottle import (  # type: ignore
    default_app,
    get,
    post,
    request,
    run,
    static_file,
)
import firebase_admin  # type: ignore
from data.firebase.firestore.firestore_ref import FirestoreRef as Ref
from usecase.interactor.download_csv_interactor import DownloadCSVInteractor
from usecase.interactor.email_update_interactor import EmailUpdateInteractor
from usecase.interactor.signin_interactor import SignInInteractor
from router.router import Router
from decorator.signin_decorator import signin_required

"""
このファイルでは、以下の3点を扱います。
- アプリ起動時の初期化処理
- 画面からの入力受付
- 入力から出力までのおおまかな流れ

データクラスとのロジックは、UseCaseに委譲します。
画面遷移のロジックは、Routerに委譲します。
"""

__will_debug: bool = __name__ == "__main__"

__root_dir: str = os.getcwd()

dictType = dict[str, Optional[Ref.valueType]]


@get("/favicon.ico")
def favicon():
    root_path = __root_dir + "/static"
    return static_file("favicon.ico", root=root_path)


if __will_debug:

    @get("/static/<filepath:path>")
    def static(filepath):
        root_path = __root_dir + "/static"
        return static_file(filepath, root=root_path)

    @get("/tmp/<filepath:path>")
    @signin_required
    def tmp(filepath):
        root_path = __root_dir + "/tmp"
        return static_file(filepath, root=root_path, download=True)

else:

    @get("/tmp/<filepath:path>", name="static_file")
    @signin_required
    def static(filepath):
        return static_file(filepath, root="/tmp", download=True)


@get("/signin")
def signin():
    return Router.template_signin_view(message=None)


@post("/signin")
def do_signin() -> None:
    # 画面からの入力を受け取る
    username = request.forms.get("username")
    password = request.forms.get("password")

    # 画面操作ユーザーをサインインさせるか判断する
    if not (type(username) == str) and (type(password) == str):
        return

    # サインインを試みる
    is_success: bool = SignInInteractor().do_signin(
        username=username, password=password
    )

    if is_success:
        Router.redirect_root_view()
    else:
        Router.redirect_signin_view()


@get("/signout")
def signout() -> None:
    SignInInteractor().signout()
    Router.redirect_root_view()


@get("/")
@signin_required
def html_index():
    return Router.template_root_view(message=None)


@post("/filter_collection")
@signin_required
def filter_collection():
    # 画面からの入力を受け取る
    collection: str = request.forms.collection
    return Router.template_filtered_result_view(collection=collection, message=None)


@post("/get_filtered_result")
@signin_required
def get_filtered_result():
    # 画面からの入力を受け取る
    collection: str = request.forms.collection
    key: str = request.forms.key
    compare: str = request.forms.compare
    value: Optional[Ref.valueType] = request.forms.value

    # CSVをダウンロードする
    is_success: bool = DownloadCSVInteractor().download_filtered_result(
        collection=collection, key=key, compare=compare, value=value
    )

    message: str = "検索条件とヒットするデータがダウンロードされました" if is_success else "検索条件とヒットするデータがありません"
    return Router.template_root_view(message)


@get("/likes")
@signin_required
def likes():
    return Router.template_likes_view(message=None)


@post("/get_followers")
@signin_required
def get_followers():
    # 画面からの入力を受け取る
    email = request.forms.get("email")
    if not (type(email) == str):
        return Router.template_likes_view(message="フォーマットが無効です")

    # CSVをダウンロードする
    is_success: bool = DownloadCSVInteractor().download_followers(email=email)

    message: str = "検索条件とヒットするデータがダウンロードされました" if is_success else "検索条件とヒットするデータがありません"
    return Router.template_likes_view(message)


@post("/get_dogs_i_followed")
@signin_required
def get_dogs_i_followed():
    # 画面からの入力を受け取る
    email = request.forms.get("email")
    if not (type(email) == str):
        return Router.template_likes_view(message="フォーマットが無効です")

    # CSVをダウンロードする
    is_success: bool = DownloadCSVInteractor().download_dogs_i_followed(email=email)

    message: str = "検索条件とヒットするデータがダウンロードされました" if is_success else "検索条件とヒットするデータがありません"
    return Router.template_likes_view(message)


@post("/get_users_follow_dog")
@signin_required
def get_users_follow_dog():
    # CSVをダウンロードする
    is_success: bool = DownloadCSVInteractor().download_users_follow_dog()

    message: str = "ヒットするデータがダウンロードされました" if is_success else "ヒットするデータがありません"
    return Router.template_likes_view(message)


@get("/update_user")
@signin_required
def update_user():
    return Router.template_update_user_view(message=None)


@post("/update_user_email")
@signin_required
def update_user_email():
    # 画面からの入力を受け取る
    current_email = request.forms.get("currrent_email")
    upcomming_email = request.forms.get("upcomming_email")

    # メールアドレスを更新する
    if not (type(current_email) == str) and (type(upcomming_email) == str):
        return Router.template_update_user_view(message="フォーマットが無効です")
    EmailUpdateInteractor().update_user_email(
        current_email=current_email, upcomming_email=upcomming_email
    )

    message = f"{current_email} が {upcomming_email} に更新されました"
    return Router.template_update_user_view(message)


"""アプリ起動時の初期化処理"""


def __init_firebase() -> None:
    certificate_path: str = (
        __root_dir + "/resource/hoge-dev.json"
        if __will_debug
        else __root_dir + "/resource/hoge-prod.json"
    )
    credential = firebase_admin.credentials.Certificate(certificate_path)
    firebase_admin.initialize_app(credential)


__init_firebase()

if __will_debug:
    run(host="localhost", port=8080, debug=True, reloader=True)
else:
    app = default_app()
