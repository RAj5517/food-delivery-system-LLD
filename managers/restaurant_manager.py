from typing import List
from models.restaurant import Restaurant


class RestaurantManager:
    _instance = None

    def __init__(self):
        self._restaurants: List[Restaurant] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = RestaurantManager()
        return cls._instance

    def add_restaurant(self, restaurant: Restaurant):
        self._restaurants.append(restaurant)

    def search_by_location(self, location: str) -> List[Restaurant]:
        return [
            restaurant
            for restaurant in self._restaurants
            if restaurant.location == location
        ]

    def get_restaurant_by_id(self, restaurant_id: str) -> Restaurant | None:
        for restaurant in self._restaurants:
            if restaurant.restaurant_id == restaurant_id:
                return restaurant
        return None
