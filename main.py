from models.dish import Dish
from models.menu_item import MenuItem
from models.menu import Menu
from models.restaurant import Restaurant
from models.user import User

from managers.restaurant_manager import RestaurantManager
from managers.order_manager import OrderManager
from managers.payment_manager import PaymentManager


def main():
    # ---------- SETUP ----------
    restaurant_manager = RestaurantManager.get_instance()
    order_manager = OrderManager.get_instance()
    payment_manager = PaymentManager.get_instance()

    # ---------- CREATE DISH ----------
    pizza = Dish("D1", "Pizza", "Cheese Pizza")

    # ---------- CREATE MENU ITEM ----------
    pizza_item = MenuItem(
        dish=pizza,
        price=250.0,
        is_available=True,
        restaurant_description="Classic cheese pizza"
    )

    # ---------- CREATE MENU ----------
    menu = Menu([pizza_item])

    # ---------- CREATE RESTAURANT ----------
    restaurant = Restaurant(
        restaurant_id="R1",
        name="Pizza Place",
        location="Bangalore",
        is_open=True,
        menu=menu
    )

    restaurant_manager.add_restaurant(restaurant)

    # ---------- CREATE USER ----------
    user = User("U1", "Sayan")

    # ---------- USER FLOW ----------
    # Create cart
    order_manager.create_cart_for_user(user, restaurant)

    # Add item to cart
    order_manager.add_item_to_cart(
        user.cart,
        pizza_item,
        quantity=2
    )

    # Place order
    order = order_manager.create_order_from_cart(user)

    print(f"Order created with status: {order.status}")

    # ---------- PAYMENT ----------
    payment_manager.initiate_payment(order, payment_method="UPI")

    print(f"Final order status: {order.status}")


if __name__ == "__main__":
    main()
