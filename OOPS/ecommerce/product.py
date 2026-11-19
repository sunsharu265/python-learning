"""
product.py - the things we sell.

OOPS concepts used here:
    - Class and constructor      : Product, __init__
    - Class variable             : total_products (shared counter)
    - Encapsulation              : __stock is private; changed only by methods
    - Inheritance                : Electronics, Clothing, Grocery are Products
    - Polymorphism (overriding)  : each child has its own get_details()
                                   and its own discount_percent()
    - Special method             : __str__
"""


class Product:
    total_products = 0                     # class variable: shared by all

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock               # private: nobody can set it to -5
        Product.total_products += 1

    # ---- encapsulation: safe doors to the private stock ----
    def get_stock(self):
        return self.__stock

    def is_available(self, quantity):
        return quantity <= self.__stock

    def reduce_stock(self, quantity):
        if quantity > self.__stock:
            print(f"Only {self.__stock} of {self.name} left.")
            return False
        self.__stock -= quantity
        return True

    def add_stock(self, quantity):
        if quantity > 0:
            self.__stock += quantity

    # ---- children override these two (polymorphism) ----
    def discount_percent(self):
        return 0                           # a normal product has no discount

    def get_details(self):
        return "General item"

    # ---- common to every product ----
    def final_price(self):
        discount = self.price * self.discount_percent() / 100
        return self.price - discount

    def __str__(self):
        return (f"{self.name} | Rs.{self.final_price():.2f} "
                f"| {self.get_details()} | Stock: {self.__stock}")


class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)       # parent sets the common part
        self.warranty_years = warranty_years       # child adds its own part

    def discount_percent(self):
        return 10

    def get_details(self):
        return f"Electronics, {self.warranty_years} year warranty"


class Clothing(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def discount_percent(self):
        return 20

    def get_details(self):
        return f"Clothing, size {self.size}"


class Grocery(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.expiry_date = expiry_date

    # No discount_percent() here, so the parent's version (0%) is used.

    def get_details(self):
        return f"Grocery, use before {self.expiry_date}"
