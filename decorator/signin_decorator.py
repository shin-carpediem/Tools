from usecase.interactor.signin_interactor import SignInInteractor
from router.router import Router


"""
ユーザーがサインインしているかどうかを確認するデコレータ
"""


def signin_required(func):
    def wrapper(*args, **kwargs):
        # 画面操作ユーザーがサインインしているか判断する
        is_user_signedin: bool = SignInInteractor().is_user_signedin()
        if is_user_signedin:
            return func(*args, **kwargs)
        else:
            Router.redirect_signin_view()

    return wrapper
