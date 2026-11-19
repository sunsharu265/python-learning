"""
payment.py - the different ways to pay.

OOPS concepts used here:
    - Abstraction   : Payment is a rule book. Every payment type MUST have pay().
    - Inheritance   : UPI, Card and CashOnDelivery are all Payments.
    - Polymorphism  : the Order just calls payment.pay(amount); each type
                      does it in its own way.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        """Try to pay. Return True if it worked, False if it failed."""
        pass


class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid Rs.{amount:.2f} using UPI ({self.upi_id}).")
        return True


class CardPayment(Payment):
    def __init__(self, card_number, card_limit):
        self.card_number = card_number
        self.card_limit = card_limit

    def pay(self, amount):
        if amount > self.card_limit:
            print(f"Card declined. Limit is Rs.{self.card_limit:.2f}.")
            return False
        self.card_limit -= amount
        print(f"Paid Rs.{amount:.2f} using card ending with {self.card_number[-4:]}.")
        return True


class CashOnDelivery(Payment):
    max_amount = 5000                      # class variable: COD limit for everyone

    def pay(self, amount):
        if amount > CashOnDelivery.max_amount:
            print(f"Cash on Delivery is only for orders up to "
                  f"Rs.{CashOnDelivery.max_amount}.")
            return False
        print(f"Please keep Rs.{amount:.2f} ready. Pay when the order arrives.")
        return True
