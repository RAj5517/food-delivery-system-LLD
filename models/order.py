from typing import List
from models.order_item import OrderItem


class Order:
    def __init__(self, order_id: str, status: str, items: List[OrderItem], total_amount: float):
        self.order_id = order_id
        self.status = status
        self.items = items
        self.total_amount = total_amount
