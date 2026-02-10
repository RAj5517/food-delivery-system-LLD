from typing import List
from models.menu_item import MenuItem


class Menu:
    def __init__(self, items: List[MenuItem]):
        self.items = items
