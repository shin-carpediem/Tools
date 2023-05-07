from itertools import chain
from typing import Optional
from data.firebase.firestore.firestore_entity import FirestoreEntity
from data.firebase.firestore.firestore_ref import FirestoreRef as Ref


"""
Firestoreコレクションから辞書の一覧に変換するトランスレータ
"""


class FirestoreToDictListTranslator:
    """Private"""

    dictType = dict[str, Optional[Ref.valueType]]

    __firestore_ref = Ref()

    def __uid_from_email(self, email: str) -> Optional[str]:
        users_docs = self.__firestore_ref.query(
            collection="users",
            key="email",
            compare="==",
            value=email,
        ).stream()
        uid_list: list[str] = [doc.id for doc in users_docs]
        return None if (uid_list == []) else uid_list[0]

    """Internal"""

    """
    `main.py` の `get_filtered_result` メソッド内で実行する。
    コレクションストリームからドキュメントの一覧を出力する。
    - parameter collection: コレクション名
    - parameter key: キー名
    - parameter compare: 演算子
    - parameter value: 値
    - returns: ドキュメントが辞書に変換された一覧
    """

    def translate_for_filtered_result(
        self,
        collection: str,
        key: str,
        compare: str,
        value: Optional[Ref.valueType],
    ) -> list[dictType]:
        casted_compare, casted_value = FirestoreEntity.convert_to_firestore_type(
            operator_alias_val=compare, value=value
        )
        docs = self.__firestore_ref.query(
            collection=collection, key=key, compare=casted_compare, value=casted_value
        ).stream()
        return [doc.to_dict() for doc in docs]

    """
    `main.py` の `get_followers` メソッド内で実行する。
    入力ユーザーの犬をフォローしている他ユーザーの一覧を出力する。
    - parameter email: メールアドレス
    - returns: `user` ドキュメントが辞書に変換された一覧
    """

    def translate_for_followers(self, email: str) -> list[dictType]:
        uid: Optional[str] = self.__uid_from_email(email)
        if uid is None:
            return []

        pets_docs = self.__firestore_ref.pets_collection_of_user(uid).stream()

        def user_id(self, user_pet_id: str) -> list[str]:
            likes_docs = self.__firestore_ref.likes_collection_of_user_pet(
                uid=uid, user_pet_id=user_pet_id
            ).stream()
            return [doc.to_dict()["user_id"] for doc in likes_docs]

        uid_nested_list: list[list[str]] = [user_id(self, doc.id) for doc in pets_docs]
        uid_chain: chain[str] = chain.from_iterable(uid_nested_list)
        uid_list: list[str] = list(uid_chain)

        return [self.__firestore_ref.user_doc(uid).get().to_dict() for uid in uid_list]

    """
    `main.py` の `get_dogs_i_followed` メソッド内で実行する。
    入力ユーザーがフォローしている犬の一覧を出力する。
    - parameter email: メールアドレス
    - returns: `pet` ドキュメントが辞書に変換された一覧
    """

    def translate_for_dogs_i_followed(self, email: str) -> list[dictType]:
        uid: Optional[str] = self.__uid_from_email(email)
        if uid is None:
            return []

        likes_docs = self.__firestore_ref.likes_collection_of_user(uid).stream()
        pet_id_list: list[str] = [doc.to_dict()["pet_id"] for doc in likes_docs]

        return [self.__firestore_ref.pet_doc(id).get().to_dict() for id in pet_id_list]

    """
    `main.py` の `get_users_follow_dog` メソッド内で実行する。
    1匹以上の犬をフォローしているユーザーの一覧を出力する。
    - returns: `user` ドキュメントが辞書に変換された一覧
    """

    def translate_for_users_follow_dog(
        self,
    ) -> list[dictType]:
        users_docs = self.__firestore_ref.users_collection().stream()

        dictType = dict[str, Optional[Ref.valueType]]

        def user(self, user_doc) -> Optional[dictType]:
            likes_collection = self.__firestore_ref.likes_collection_of_user(
                user_doc.id
            )
            likes_list: list = list(likes_collection.get())
            likes_count: int = len(likes_list)
            if likes_count == 0:
                return None

            user_dict: dictType = user_doc.to_dict()
            user_dict["likes_count"] = likes_count
            return user_dict

        user_optional_list: list[Optional[dictType]] = [
            user(self, doc) for doc in users_docs
        ]
        return [
            user_optional
            for user_optional in user_optional_list
            if (user_optional is not None)
        ]
