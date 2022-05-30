from typing import Dict

from src.repositories.database_repository import DatabaseRepository


class PropertyRepository:
    def __init__(self) -> None:
        self.database_repository = DatabaseRepository()

    def find_property_by_id(self, property_id: str) -> Dict[str, any]:
        properties = self.database_repository.get_properties_collection()
        return properties.document(property_id).get().to_dict()

    def update_property_by_id(
        self, property_id: str, property: Dict[str, any]
    ) -> Dict[str, any]:
        properties = self.database_repository.get_properties_collection()
        properties.document(property_id).update(property)
        return self.find_property_by_id(property_id)
