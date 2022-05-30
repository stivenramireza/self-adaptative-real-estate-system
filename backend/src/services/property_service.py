from typing import Dict

from flask import abort

from src.repositories.property_repository import PropertyRepository


class PropertyService:
    def __init__(self) -> None:
        self.property_repository = PropertyRepository()

    def get_property_by_id(self, property_id: int) -> None:
        property = self.property_repository.find_property_by_id(property_id)

        if not property:
            abort(404)

        return property

    def increment_property_visits(self, property: Dict[str, any]) -> None:
        property.update({'Visits': property.get('Visits') + 1})

    def increment_property_price(self, property: Dict[str, any]) -> None:
        if property.get('Visits') % 5 == 0:
            property.update({'Price': property.get('Price') + 100_000})

    def control_property_variables(self, property_id: int) -> Dict[str, any]:
        property = self.get_property_by_id(property_id)

        self.increment_property_visits(property)
        self.increment_property_price(property)

        return self.property_repository.update_property_by_id(
            property_id, property
        )
