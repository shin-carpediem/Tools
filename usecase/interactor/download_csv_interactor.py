from typing import Optional
from data.firebase.firestore.firestore_entity import FirestoreEntity
from data.firebase.firestore.firestore_ref import FirestoreRef as Ref
from usecase.translator.dictlist_to_csv_translator import DictListToCsvTranslator
from usecase.translator.firestore_to_dictlist_translator import (
    FirestoreToDictListTranslator,
)
from router.router import Router


class DownloadCSVInteractor:
    """Internal"""

    def download_filtered_result(
        self,
        collection: str,
        key: str,
        compare: str,
        value: Optional[Ref.valueType],
    ) -> bool:
        dictType = dict[str, Optional[Ref.valueType]]

        # Firestoreからデータを取得する
        fieldnames: list[str] = FirestoreEntity.convert_to_fieldnames(collection)
        data_for_csv: list[
            dictType
        ] = FirestoreToDictListTranslator().translate_for_filtered_result(
            collection=collection, key=key, compare=compare, value=value
        )

        # 取得したデータからCSVを生成する
        if data_for_csv == []:
            return False
        filename: str = DictListToCsvTranslator().translate_from_dict_list(
            fieldnames=fieldnames, dict_list=data_for_csv
        )

        # 生成したCSVを改めてダウンロードする
        Router.download_csv(filename)
        return True

    def download_followers(self, email: str) -> bool:
        dictType = dict[str, Optional[Ref.valueType]]

        # Firestoreからデータを取得する
        fieldnames: list[str] = FirestoreEntity.UserDoc.fieldnames
        data_for_csv: list[
            dictType
        ] = FirestoreToDictListTranslator().translate_for_followers(email)

        # 取得したデータからCSVを生成する
        if data_for_csv == []:
            return False
        filename: str = DictListToCsvTranslator().translate_from_dict_list(
            fieldnames=fieldnames, dict_list=data_for_csv
        )

        # 生成したCSVを改めてダウンロードする
        Router.download_csv(filename)
        return True

    def download_dogs_i_followed(self, email: str) -> bool:
        dictType = dict[str, Optional[Ref.valueType]]

        # Firestoreからデータを取得する
        fieldnames: list[str] = FirestoreEntity.PetDoc.fieldnames
        data_for_csv: list[
            dictType
        ] = FirestoreToDictListTranslator().translate_for_dogs_i_followed(email)

        # 取得したデータからCSVを生成する
        if data_for_csv == []:
            return False
        filename: str = DictListToCsvTranslator().translate_from_dict_list(
            fieldnames=fieldnames, dict_list=data_for_csv
        )

        # 生成したCSVを改めてダウンロードする
        Router.download_csv(filename)
        return True

    def download_users_follow_dog(self) -> bool:
        dictType = dict[str, Optional[Ref.valueType]]

        # Firestoreからデータを取得する
        fieldnames: list[str] = FirestoreEntity.UserDoc.fieldnames + ["likes_count"]
        data_for_csv: list[
            dictType
        ] = FirestoreToDictListTranslator().translate_for_users_follow_dog()

        # 取得したデータからCSVを生成する
        if data_for_csv == []:
            return False
        filename: str = DictListToCsvTranslator().translate_from_dict_list(
            fieldnames=fieldnames, dict_list=data_for_csv
        )

        # 生成したCSVを改めてダウンロードする
        Router.download_csv(filename)
        return True
