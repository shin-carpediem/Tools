from dotenv import load_dotenv  # type: ignore

load_dotenv()
from settings import SECRET_KEY
from bottle import request, response  # type: ignore
from data.session_cookie.repository.session_cookie_repository import (
    SessionCookieRepository,
)


class SessionCookieDataStore(SessionCookieRepository):
    """Private"""

    __session_cookie_name = "account"

    """SessionCookieRepository"""

    def set_cookie(self, key: str) -> None:
        # Cookieはクライアント側で改変できてしまうので、
        # 本来は値そのものではなく署名キーを引数に渡すべき。
        response.set_cookie(
            self.__session_cookie_name,
            key,
            secret=SECRET_KEY,
            secure=True,
            httponly=True,
        )

    def get_cookie(self):
        return request.get_cookie(self.__session_cookie_name, secret=SECRET_KEY)

    def delete_cookie(self) -> None:
        response.delete_cookie(self.__session_cookie_name)
