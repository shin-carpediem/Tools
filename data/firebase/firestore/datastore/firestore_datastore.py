from data.firebase.firestore.repository.firestore_repository import FirestoreRepository
from data.firebase.firestore.firestore_ref import FirestoreRef


class FirestoreDataStore(FirestoreRepository):
    """FirestoreRepository"""

    def update_user_email(self, uid: str, email: str) -> None:
        user_doc = FirestoreRef().user_doc(uid)
        user_doc.update({"email": email})
