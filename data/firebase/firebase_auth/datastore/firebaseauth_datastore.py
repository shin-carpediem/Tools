from firebase_admin import auth  # type: ignore
from data.firebase.firebase_auth.repository.firebaseauth_repository import (
    FirebaseAuthRepository,
)


class FirebaseAuthDataStore(FirebaseAuthRepository):
    """FirebaseAuthRepository"""

    def update_user(self, uid: str, email: str) -> None:
        auth.update_user(uid, email=email)
