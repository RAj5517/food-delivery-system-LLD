from models.menu import Menu


class Restaurant:
    def __init__(
        self,
        restaurant_id: str,
        name: str,
        location: str,
        is_open: bool,
        menu: Menu
    ):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.is_open = is_open
        self.menu = menu
