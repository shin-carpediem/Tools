from typing import Optional
from data.firebase.firestore.firestore_ref import FirestoreRef as Ref


class FirestoreEntity:
    """
    /guardianships/{id}
    """

    class GuardianshipsDoc:
        fieldnames = [
            "created_at",
            "notification_id",
            "pet_id",
            "search_labels",
            "sent_by",
            "sent_to",
            "status",
        ]

    """
    /lost_pets/{id}
    """

    class LostPetsDoc:
        fieldnames = [
            "address_block",
            "created_at",
            "identification_photos",
            "is_active",
            "lost_at",
            "note",
            "pet_id",
            "user_id",
            "user_pet_id",
        ]

    """
    /notification_channel_subscriptions/{id}
    """

    class NotificationChannelSubscriptionsDoc:
        fieldnames = [
            "channel_name",
            "user_id",
        ]

    """
    /pets/{id}
    """

    class PetDoc:
        fieldnames = [
            "user_pet_id",
            "breed",
            "breed_info",
            "date_of_birth",
            "dog_card_notes",
            "color",
            "ear_type",
            "feeding_detail",
            "hair_color_primary",
            "hair_color_secondary",
            "liked_users",
            "hospital",
            "medical_history",
            "medicine",
            "microchip_number",
            "name",
            "nose_id",
            "nose_registered",
            "notes",
            "photo",
            "rabies_injection_status",
            "reference_id",
            "registration_status",
            "saloon",
            "sex",
            "spay_status",
            "user_id",
            "video_url_1",
            "video_url_2",
            "weight",
            "is_lost",
            "created_at",
            "updated_at",
        ]

    """
    /user_targeted_notifications/{id}
    """

    class UserTargetedNotificationsDoc:
        fieldnames = [
            "associated_user_id",
            "created_at",
            "notification_body",
            "notification_data",
            "notification_title",
            "sender_id",
            "type",
        ]

    """
    /users/{id}
    """

    class UserDoc:
        fieldnames = [
            "address",
            "address_block",
            "email",
            "id",
            "likes",
            "sns",
            "name",
            "note",
            "phone_number",
            "photo",
            "fcm_token",
            "read_notifications",
            "created_at",
            "last_login",
        ]

    collection_list = [
        "guardianships",
        "lost_pets",
        "notification_channel_subscriptions",
        "pets",
        "user_targeted_notifications",
        "users",
    ]

    operator_alias = {
        "==": "(==) 次に等しい",
        "!=": "(!=) 等しくない",
        ">=": "(>=) 次の値以上",
        "<=": "(<=) 次の値以下",
    }

    """
    入力フォームの内容(`Collection`)を、Firestore のドキュメントフィールド名に変換する。
    """

    @classmethod
    def convert_to_fieldnames(cls, collection: str) -> list[str]:
        if collection == "guardianships":
            return FirestoreEntity.GuardianshipsDoc.fieldnames
        elif collection == "lost_pets":
            return FirestoreEntity.LostPetsDoc.fieldnames
        elif collection == "notification_channel_subscriptions":
            return FirestoreEntity.NotificationChannelSubscriptionsDoc.fieldnames
        elif collection == "pets":
            return FirestoreEntity.PetDoc.fieldnames
        elif collection == "user_targeted_notifications":
            return FirestoreEntity.UserTargetedNotificationsDoc.fieldnames
        elif collection == "users":
            return FirestoreEntity.UserDoc.fieldnames
        else:
            raise ValueError("不正なコレクション名です")

    """
    入力フォームの内容(`Compare`, `Value`)を、Firestore のコレクションをクエリできる型に変換する。
    """

    @classmethod
    def convert_to_firestore_type(
        cls, operator_alias_val: str, value: Optional[Ref.valueType]
    ) -> tuple[str, Ref.valueType]:
        # compare(演算子)は辞書型のバリューを取得しているのでキーに変換する。
        compare: str = [
            k for k, val in cls.operator_alias.items() if val == operator_alias_val
        ][0]

        if value is None:
            value = ""

        return compare, value
