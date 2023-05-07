from typing import Union
from firebase_admin import firestore  # type: ignore

"""
Firestoreのリファレンス一覧
"""


class FirestoreRef:
    """Private"""

    def __db(self):
        return firestore.client()

    """ Internal """

    """
    /pets/*
    """

    def pets_collection(self):
        return self.__db().collection("pets")

    """
    /pets/{pet_id}
    """

    def pet_doc(self, pet_id: str):
        return self.pets_collection().document(pet_id)

    """
    /users/*
    """

    def users_collection(self):
        return self.__db().collection("users")

    """
    /users/{uid}
    """

    def user_doc(self, uid: str):
        return self.users_collection().document(uid)

    """
    /users/{uid}/pets/*
    """

    def pets_collection_of_user(self, uid: str):
        return self.user_doc(uid).collection("pets")

    """
    /users/{uid}/pets/{user_pet_id}/likes/*
    """

    def likes_collection_of_user_pet(self, uid: str, user_pet_id: str):
        return (
            self.user_doc(uid)
            .collection("pets")
            .document(user_pet_id)
            .collection("likes")
        )

    """
    /users/{uid}/likes/*
    """

    def likes_collection_of_user(self, uid: str):
        return self.user_doc(uid).collection("likes")

    """
    ルート直下のコレクションに対するクエリ
    """

    valueType = Union[str, int, float, bool]

    def query(
        self,
        collection: str,
        key: str,
        compare: str,
        value: valueType,
    ):
        return (
            self.__db().collection(collection)
            # クエリする
            .where(
                key,
                compare,
                value,
            )
        )
