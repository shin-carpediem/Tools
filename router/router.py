from typing import Optional
from bottle import (  # type: ignore
    redirect,
    jinja2_template as template,
)
from data.firebase.firestore.firestore_entity import FirestoreEntity

"""
画面遷移を管理するクラス
"""


class Router:
    """Redirect to Path"""

    @classmethod
    def redirect_root_view(cls) -> None:
        redirect("/")

    @classmethod
    def redirect_signin_view(cls) -> None:
        redirect("/signin")

    @classmethod
    def download_csv(cls, filename: str) -> None:
        redirect(filename)

    """Render Context"""

    @classmethod
    def template_signin_view(cls, message: Optional[str]):
        return template("signin.j2", message=message)

    @classmethod
    def template_root_view(cls, message: Optional[str]):
        collection: list[str] = FirestoreEntity.collection_list

        return template("filter_collection.j2", collection=collection, message=message)

    @classmethod
    def template_filtered_result_view(cls, collection: str, message: Optional[str]):
        key: list[str] = FirestoreEntity.convert_to_fieldnames(collection)
        compare: dict[str, str] = FirestoreEntity.operator_alias

        return template(
            "get_filtered_result.j2",
            collection=collection,
            key=key,
            compare=compare,
            message=message,
        )

    @classmethod
    def template_likes_view(cls, message: Optional[str]):
        return template("likes.j2", message=message)

    @classmethod
    def template_update_user_view(cls, message: Optional[str]):
        return template("update_user.j2", message=message)
