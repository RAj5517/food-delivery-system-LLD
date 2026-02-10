from models.payment import Payment
from managers.order_manager import OrderManager
from factories.payment_factory import PaymentFactory


class PaymentManager:
    _instance = None

    def __init__(self):
        self._payments = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PaymentManager()
        return cls._instance

    def initiate_payment(self, order, payment_method: str):
        strategy = PaymentFactory.get_strategy(payment_method)

        result = strategy.pay(order.total_amount)

        payment = Payment(
            payment_id=f"PAY-{len(self._payments) + 1}",
            order_id=order.order_id,
            amount=order.total_amount,
            status=result,
            method=payment_method
        )

        self._payments.append(payment)

        order_manager = OrderManager.get_instance()

        if result == "SUCCESS":
            order_manager.update_order_status(order, "CONFIRMED")
        else:
            order_manager.update_order_status(order, "PAYMENT_FAILED")
