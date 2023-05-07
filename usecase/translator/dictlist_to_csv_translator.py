import csv, random
from typing import Literal, Optional
import bottle  # type: ignore
from data.firebase.firestore.firestore_ref import FirestoreRef as Ref

"""
辞書の一覧からCSVに変換するトランスレータ
"""


class DictListToCsvTranslator:
    """Private"""

    dictType = dict[str, Optional[Ref.valueType]]

    def __filename(self) -> str:
        return "/tmp/" + str(random.randint(1000, 9999)) + ".csv"

    """Internal"""

    """
    辞書の一覧からCSVを出力する。
    - parameter fieldnames: CSVのヘッダー
    - parameter dict_list: CSVに変換したい辞書の一覧
    - returns: 出力先のパス
    """

    def translate_from_dict_list(
        self, fieldnames: list[str], dict_list: list[dictType]
    ) -> str:
        filename: str = self.__filename()

        with open(filename, "w", encoding="utf-8_sig", newline="") as file:
            extrasaction: Literal["raise", "ignore"] = (
                "raise" if bottle.DEBUG else "ignore"
            )
            writer = csv.DictWriter(
                file, fieldnames=fieldnames, extrasaction=extrasaction
            )
            writer.writeheader()
            writer.writerows(dict_list)

        return filename
