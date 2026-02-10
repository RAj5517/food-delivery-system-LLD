class OrderItem:
    def __init__(self, dish_name: str, price_snapshot: float, quantity: int):
        self.dish_name = dish_name
        self.price_snapshot = price_snapshot
        self.quantity = quantity
