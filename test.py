import unittest
import firebase_admin  # type: ignore
from data.firebase.firestore.firestore_entity import FirestoreEntity
from usecase.translator.firestore_to_dictlist_translator import (
    FirestoreToDictListTranslator,
)


class FirestoreEntityTest(unittest.TestCase):
    """
    `convert_to_firestore_type` メソッドのテスト
    """

    def test_convert_to_firestore_type(self) -> None:
        self.assertEqual(
            FirestoreEntity.convert_to_firestore_type(
                operator_alias_val="(==) 次に等しい", value="大阪市"
            ),
            ("==", "大阪市"),
        )
        self.assertEqual(
            FirestoreEntity.convert_to_firestore_type(
                operator_alias_val="(==) 次に等しい", value=None
            ),
            ("==", ""),
        )
        print("✅ Tested `convert_to_firestore_type`")


class FirestoreToDictListTranslatorTest(unittest.TestCase):
    """
    `translate_for_followers` メソッドのテスト
    """

    def test_translate_for_followers(self) -> None:
        self.assertEqual(
            len(
                FirestoreToDictListTranslator().translate_for_followers(
                    email="manas.shtha@gmail.com"
                )
            ),
            4,
        )
        print("✅ Tested `translate_for_followers`")

    """
    `translate_for_dogs_i_followed` メソッドのテスト
    """

    def test_translate_for_dogs_i_followed(self) -> None:
        self.assertEqual(
            len(
                FirestoreToDictListTranslator().translate_for_dogs_i_followed(
                    email="manas.shtha@gmail.com"
                )
            ),
            2,
        )
        print("✅ Tested `translate_for_dogs_i_followed`")

    """
    `translate_for_users_follow_dog` メソッドのテスト
    """

    def test_translate_for_users_follow_dog(self) -> None:
        self.assertEqual(
            len(FirestoreToDictListTranslator().translate_for_users_follow_dog()),
            6,
        )
        print("✅ Tested `translate_for_users_follow_dog`")


"""テスト実行時の初期化処理"""


def __init_firebase_dev() -> None:
    credential = firebase_admin.credentials.Certificate("./resource/hoge-dev.json")
    firebase_admin.initialize_app(credential)
    print("🏃 Initialized Firebase Dev App")


def __run_test() -> None:
    unittest.main()


if __name__ == "__main__":
    __init_firebase_dev()
    __run_test()
