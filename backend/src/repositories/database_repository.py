from src.config.database import FirestoreConnection


class DatabaseRepository:
    def get_properties_collection(self) -> object:
        return FirestoreConnection().get_instance().collection('Inmuebles')
