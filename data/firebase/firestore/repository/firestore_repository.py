from abc import ABC, abstractmethod

"""
FirestoreのI/Oプロトコル
"""


class FirestoreRepository(ABC):
    """
    `user` ドキュメント内の `email` フィールドを更新する
    - parameter id: `user` ドキュメントのID
    - parameter email: 新しいメールアドレス
    """

    @abstractmethod
    def update_user_email(self, uid: str, email: str) -> None:
        pass
