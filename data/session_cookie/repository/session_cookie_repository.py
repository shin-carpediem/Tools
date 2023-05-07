from abc import ABC, abstractmethod

"""
セッションCookieのI/Oプロトコル
"""


class SessionCookieRepository(ABC):
    """
    セッションCookieをセットする
    - parameter key: セッションCookieのキー
    """

    @abstractmethod
    def set_cookie(self, key: str) -> None:
        pass

    """
    セッションCookieを取得する
    - returns: セッションCookie
    """

    @abstractmethod
    def get_cookie(self):
        pass

    """
    セッションCookieを削除する
    """

    @abstractmethod
    def delete_cookie(self) -> None:
        pass
