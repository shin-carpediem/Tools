from dotenv import load_dotenv  # type: ignore

load_dotenv()
from settings import USERNAME, PASSWORD
from data.session_cookie.repository.session_cookie_repository import (
    SessionCookieRepository,
)
from data.session_cookie.datastore.session_cookie_datastore import (
    SessionCookieDataStore,
)


"""
ユーザーのサインインを管理するクラス
"""


class SignInInteractor:
    """Private"""

    __repository: SessionCookieRepository

    def __init__(
        self, repository: SessionCookieRepository = SessionCookieDataStore()
    ) -> None:
        self.__repository = repository

    """Internal"""

    """
    サインインを試みる
    - parameter username: ユーザー名
    - parameter password: パスワード
    - returns: サインインに成功したか
    """

    def do_signin(self, username: str, password: str) -> bool:
        # 限られたユーザーにしかサインインしてほしくないので、
        # `username`, `password` が、
        # あらかじめ用意した特定の文字列に一致するかどうかで認証する。
        should_user_signed_in: bool = username == USERNAME and password == PASSWORD

        if should_user_signed_in:
            # サインインさせる
            self.__repository.set_cookie(key=username)
            return True
        else:
            # サインアウトさせる
            self.signout()
            return False

    """
    ユーザーがサインインしているか
    - returns: ユーザーがサインインしているか
    """

    def is_user_signedin(self) -> bool:
        cookie = self.__repository.get_cookie()
        return False if cookie is None else True

    """
    ユーザーをサインアウトさせる
    """

    def signout(self) -> None:
        self.__repository.delete_cookie()
