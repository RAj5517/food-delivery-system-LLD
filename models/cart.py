from typing import List
from models.cart_item import CartItem
from models.restaurant import Restaurant


class Cart:
    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant
        self.items: List[CartItem] = []
