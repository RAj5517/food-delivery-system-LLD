class NotificationService:

    @staticmethod
    def send_order_confirmation(order):
        print(f"[NOTIFICATION] Order {order.order_id} confirmed")

    @staticmethod
    def send_payment_failure(order):
        print(f"[NOTIFICATION] Payment failed for order {order.order_id}")
