from src.config.database import FirestoreConnection


class DatabaseRepository:
    def __init__(self) -> None:
        self.firestore_conn = FirestoreConnection()

    def get_properties_collection(self) -> object:
        return self.firestore_conn.get_instance().collection('Inmuebles')
