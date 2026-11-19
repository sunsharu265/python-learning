"""
cart.py - the shopping cart.

OOPS concepts used here:
    - Composition     : a Cart HAS products (list of items)
    - Polymorphism    : product.final_price() works for every product type
    - Special method  : __len__ so that len(cart) works
"""


class Cart:
    def __init__(self):
        # Each item is a dictionary: {"product": <Product object>, "quantity": 2}
        self.items = []

    def add_product(self, product, quantity=1):
        if not product.is_available(quantity):
            print(f"Sorry, only {product.get_stock()} of {product.name} in stock.")
            return

        # If the product is already in the cart, just increase the quantity.
        for item in self.items:
            if item["product"] is product:
                item["quantity"] += quantity
                print(f"Added {quantity} more {product.name} to cart.")
                return

        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} x {product.name} to cart.")

    def remove_product(self, product_name):
        for item in self.items:
            if item["product"].name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from cart.")
                return
        print(f"{product_name} is not in the cart.")

    def total_amount(self):
        total = 0
        for item in self.items:
            # We do not check if it is Electronics or Clothing.
            # Every product knows its own final price. (polymorphism)
            total += item["product"].final_price() * item["quantity"]
        return total

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def show(self):
        print("\n--- Your Cart ---")
        if self.is_empty():
            print("Cart is empty.")
            return
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            line_total = product.final_price() * quantity
            print(f"{product.name} x {quantity} = Rs.{line_total:.2f}")
        print(f"Cart Total: Rs.{self.total_amount():.2f}")

    def __len__(self):
        return len(self.items)
