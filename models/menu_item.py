from models.dish import Dish


class MenuItem:
    def __init__(
        self,
        dish: Dish,
        price: float,
        is_available: bool,
        restaurant_description: str
    ):
        self.dish = dish
        self.price = price
        self.is_available = is_available
        self.restaurant_description = restaurant_description
