from strategies.payment_strategy import PaymentStrategy


class UpiPayment(PaymentStrategy):

    def pay(self, amount: float) -> str:
        print(f"[UPI] Paying amount: {amount}")
        return "SUCCESS"
