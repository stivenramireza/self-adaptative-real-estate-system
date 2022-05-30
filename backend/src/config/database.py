from firebase_admin import credentials, initialize_app, firestore


firebase_credentials = credentials.Certificate('secrets.json')
initialize_app(firebase_credentials)


class FirestoreConnection:
    def get_instance(self) -> object:
        return firestore.client()
