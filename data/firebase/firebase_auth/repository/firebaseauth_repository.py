from abc import ABC, abstractmethod


"""
FirebaseAuthenticationのI/Oプロトコル
"""


class FirebaseAuthRepository(ABC):
    """
    ユーザーのメールアドレスを更新する
    - parameter uid: UUID
    - parameter email: 新しいメールアドレス
    """

    @abstractmethod
    def update_user(self, uid: str, email: str) -> None:
        pass
