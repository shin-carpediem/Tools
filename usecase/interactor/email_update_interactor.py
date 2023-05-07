from data.firebase.firebase_auth.repository.firebaseauth_repository import (
    FirebaseAuthRepository,
)
from data.firebase.firebase_auth.datastore.firebaseauth_datastore import (
    FirebaseAuthDataStore,
)
from data.firebase.firestore.repository.firestore_repository import FirestoreRepository
from data.firebase.firestore.datastore.firestore_datastore import FirestoreDataStore
from data.firebase.firestore.firestore_ref import FirestoreRef


"""
ユーザーのメールアドレスを更新するクラス
"""
"""
ユーザーのメールアドレスを更新するには、
①
FirebaseAuthenticationで認証されているメールアドレス
②
Firestoreの /users/{user_id} ドキュメントにある
`email` フィールドに保存されているメールアドレス
のそれぞれを更新する必要があります。

このプロトコルではそれら①②の更新を担います。
"""


class EmailUpdateInteractor:
    """Private"""

    __auth_repository: FirebaseAuthRepository

    __firestore_repository: FirestoreRepository

    def __init__(
        self,
        auth_repository: FirebaseAuthRepository = FirebaseAuthDataStore(),
        firestore_repository: FirestoreRepository = FirestoreDataStore(),
    ) -> None:
        self.__auth_repository = auth_repository
        self.__firestore_repository = firestore_repository

    __firestore_ref = FirestoreRef()

    """Internal"""

    """
    ユーザーのメールアドレスを更新する
    - parameter current_email: 現在のメールアドレス
    - parameter upcomming_email: 更新後のメールアドレス
    """

    def update_user_email(self, current_email: str, upcomming_email: str) -> None:
        if current_email == upcomming_email:
            return

        user_docs = self.__firestore_ref.query(
            collection="users",
            key="email",
            compare="==",
            value=current_email,
        ).stream()
        uid_list: list[str] = [doc.id for doc in user_docs]
        if uid_list == []:
            return
        uid: str = uid_list[0]

        self.__auth_repository.update_user(uid=uid, email=upcomming_email)
        self.__firestore_repository.update_user_email(uid=uid, email=upcomming_email)
