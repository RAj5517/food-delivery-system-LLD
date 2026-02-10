from strategies.payment_strategy import PaymentStrategy


class CardPayment(PaymentStrategy):

    def pay(self, amount: float) -> str:
        print(f"[CARD] Paying amount: {amount}")
        return "SUCCESS"
