"""
customer.py - the person who shops.

OOPS concepts used here:
    - Composition    : a Customer HAS a Cart and HAS a list of orders
    - Encapsulation  : __password is private; we only allow checking it
"""

from cart import Cart


class Customer:
    def __init__(self, name, email, address, password):
        self.name = name
        self.email = email
        self.address = address
        self.__password = password         # private: never shown to anyone
        self.cart = Cart()                 # every customer gets their own cart
        self.orders = []                   # order history

    def check_password(self, password):
        # We never give the password out. We only answer: correct or not?
        return password == self.__password

    def show_order_history(self):
        print(f"\n--- Order history of {self.name} ---")
        if len(self.orders) == 0:
            print("No orders yet.")
            return
        for order in self.orders:
            print(order)

    def __str__(self):
        return f"{self.name} ({self.email})"
