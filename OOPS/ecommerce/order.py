"""
order.py - one purchase made by a customer.

OOPS concepts used here:
    - Composition     : an Order HAS a customer, items and a payment
    - Class variable  : next_order_number gives every order a new number
    - Encapsulation   : __status is private; it changes only through methods
                        (nobody can jump from "Cancelled" to "Delivered")
    - Special method  : __str__
"""


class Order:
    next_order_number = 1001               # shared by all orders
    delivery_charge = 40
    free_delivery_above = 500

    def __init__(self, customer):
        self.customer = customer
        self.items = list(customer.cart.items)     # copy of the cart items
        self.order_number = Order.next_order_number
        Order.next_order_number += 1
        self.__status = "Created"

    def get_status(self):
        return self.__status

    def items_total(self):
        total = 0
        for item in self.items:
            total += item["product"].final_price() * item["quantity"]
        return total

    def delivery_fee(self):
        if self.items_total() >= Order.free_delivery_above:
            return 0
        return Order.delivery_charge

    def grand_total(self):
        return self.items_total() + self.delivery_fee()

    def place(self, payment):
        """Pay for the order. 'payment' can be ANY kind of Payment object."""
        if self.__status not in ["Created", "Payment Failed"]:
            print(f"Order #{self.order_number} is already '{self.__status}'.")
            return False

        if len(self.items) == 0:
            print("Cannot place an order with an empty cart.")
            return False

        if not payment.pay(self.grand_total()):    # polymorphism
            self.__status = "Payment Failed"
            print(f"Order #{self.order_number} was not placed.")
            return False

        # Payment worked: take the items out of the shop's stock.
        for item in self.items:
            item["product"].reduce_stock(item["quantity"])

        self.__status = "Placed"
        self.customer.orders.append(self)
        self.customer.cart.clear()
        print(f"Order #{self.order_number} placed successfully!")
        return True

    def ship(self):
        if self.__status == "Placed":
            self.__status = "Shipped"
            print(f"Order #{self.order_number} has been shipped.")
        else:
            print(f"Cannot ship. Order status is '{self.__status}'.")

    def deliver(self):
        if self.__status == "Shipped":
            self.__status = "Delivered"
            print(f"Order #{self.order_number} delivered to {self.customer.address}.")
        else:
            print(f"Cannot deliver. Order status is '{self.__status}'.")

    def cancel(self):
        if self.__status == "Placed":
            # Put the items back into the shop's stock.
            for item in self.items:
                item["product"].add_stock(item["quantity"])
            self.__status = "Cancelled"
            print(f"Order #{self.order_number} cancelled. Money will be refunded.")
        else:
            print(f"Cannot cancel. Order status is '{self.__status}'.")

    def print_bill(self):
        print(f"\n======= BILL: Order #{self.order_number} =======")
        print(f"Customer: {self.customer.name}")
        print(f"Address : {self.customer.address}")
        print("-" * 40)
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            line_total = product.final_price() * quantity
            print(f"{product.name} x {quantity} = Rs.{line_total:.2f}")
        print("-" * 40)
        print(f"Items Total : Rs.{self.items_total():.2f}")
        print(f"Delivery    : Rs.{self.delivery_fee():.2f}")
        print(f"Grand Total : Rs.{self.grand_total():.2f}")
        print(f"Status      : {self.__status}")
        print("=" * 40)

    def __str__(self):
        return (f"Order #{self.order_number} | {len(self.items)} item(s) "
                f"| Rs.{self.grand_total():.2f} | {self.__status}")
