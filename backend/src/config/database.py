from firebase_admin import credentials, initialize_app, firestore

CREDENTIALS = 'secrets.json'


class FirestoreConnection:
    def __init__(self) -> None:
        self.credentials = credentials.Certificate(CREDENTIALS)

    def connect(self) -> object:
        initialize_app(self.credentials)

    def get_instance(self) -> object:
        return firestore.client()
