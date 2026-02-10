from strategies.upi_payment import UpiPayment
from strategies.card_payment import CardPayment


class PaymentFactory:

    @staticmethod
    def get_strategy(method: str):
        if method == "UPI":
            return UpiPayment()

        if method == "CARD":
            return CardPayment()

        raise Exception("Unsupported payment method")
