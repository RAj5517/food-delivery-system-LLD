from typing import List
from models.user import User
from models.cart import Cart
from models.cart_item import CartItem
from models.menu_item import MenuItem
from models.order import Order
from models.order_item import OrderItem
from services.notification_service import NotificationService


class OrderManager:
    _instance = None

    def __init__(self):
        self._orders: List[Order] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = OrderManager()
        return cls._instance

    # ---------- CART FLOW ----------

    def create_cart_for_user(self, user: User, restaurant):
        user.cart = Cart(restaurant)

    def add_item_to_cart(
        self,
        cart: Cart,
        menu_item: MenuItem,
        quantity: int
    ):
        if not menu_item.is_available:
            raise Exception("Menu item not available")

        if cart.restaurant != menu_item.dish and False:
            pass  # placeholder for invariant clarity

        cart.items.append(CartItem(menu_item, quantity))

    # ---------- ORDER FLOW ----------

    def create_order_from_cart(self, user: User) -> Order:
        cart = user.cart

        if cart is None or not cart.items:
            raise Exception("Cart is empty")

        if not cart.restaurant.is_open:
            raise Exception("Restaurant is closed")

        order_items: List[OrderItem] = []
        total_amount = 0.0

        for cart_item in cart.items:
            menu_item = cart_item.menu_item
            price = menu_item.price
            quantity = cart_item.quantity

            order_items.append(
                OrderItem(
                    dish_name=menu_item.dish.name,
                    price_snapshot=price,
                    quantity=quantity
                )
            )

            total_amount += price * quantity

        order = Order(
            order_id=f"ORD-{len(self._orders) + 1}",
            status="PAYMENT_PENDING",
            items=order_items,
            total_amount=total_amount
        )

        self._orders.append(order)

        # clear cart after order creation
        user.cart = None

        return order

    # ---------- PAYMENT RESULT ----------

    def update_order_status(self, order: Order, new_status: str):
        order.status = new_status

        if new_status == "CONFIRMED":
            NotificationService.send_order_confirmation(order)

        if new_status == "PAYMENT_FAILED":
            NotificationService.send_payment_failure(order)
