"""
main.py - run this file to see the whole online shop working.

    Run from the pythonLearning folder:
        python OOPS/ecommerce/main.py

The story:
    1. The shop adds products.
    2. A customer registers and logs in.
    3. She adds products to her cart.
    4. She places an order and pays.
    5. The order is shipped and delivered.
    6. A second customer shows what happens when things go wrong.
"""

from product import Product, Electronics, Clothing, Grocery
from customer import Customer
from order import Order
from payment import UPIPayment, CardPayment, CashOnDelivery


def show_products(products):
    print("\n--- Products in our shop ---")
    number = 1
    for product in products:
        print(f"{number}. {product}")       # print() uses Product.__str__
        number += 1


def main():
    # ---- 1. The shop adds products (objects of different classes) ----
    phone = Electronics("Samsung Phone", 15000, 5, warranty_years=1)
    earphones = Electronics("Earphones", 800, 10, warranty_years=1)
    saree = Clothing("Cotton Saree", 1200, 8, size="Free")
    tshirt = Clothing("T-Shirt", 500, 20, size="M")
    rice = Grocery("Rice 5kg", 350, 30, expiry_date="Dec 2027")
    notebook = Product("Notebook", 60, 100)

    products = [phone, earphones, saree, tshirt, rice, notebook]
    show_products(products)
    print("Total products in shop:", Product.total_products)

    # ---- 2. A customer registers and logs in ----
    priya = Customer("Priya", "priya@example.com", "12 Gandhi Street, Coimbatore", "priya123")
    print("\nWelcome,", priya)
    print("Login with wrong password:", priya.check_password("hello"))
    print("Login with right password:", priya.check_password("priya123"))

    # ---- 3. She adds products to her cart ----
    print()
    priya.cart.add_product(saree, 1)
    priya.cart.add_product(rice, 2)
    priya.cart.add_product(notebook, 5)
    priya.cart.add_product(phone, 50)           # more than the stock
    priya.cart.add_product(tshirt, 1)
    priya.cart.remove_product("T-Shirt")        # she changed her mind
    priya.cart.show()
    print("Different items in cart:", len(priya.cart))    # uses Cart.__len__

    # ---- 4. She places the order and pays by UPI ----
    print()
    order1 = Order(priya)
    order1.place(UPIPayment("priya@upi"))
    order1.print_bill()

    # ---- 5. The order travels to her home ----
    print()
    order1.deliver()                            # too early: not shipped yet
    order1.ship()
    order1.deliver()
    print("Rice stock after the order:", rice.get_stock())

    # ---- 6. A second customer: when things go wrong ----
    arun = Customer("Arun", "arun@example.com", "5 Nehru Nagar, Chennai", "arun@456")
    print("\nWelcome,", arun)
    arun.cart.add_product(phone, 1)
    arun.cart.add_product(earphones, 2)
    arun.cart.show()

    print()
    order2 = Order(arun)
    order2.place(CashOnDelivery())              # too costly for COD
    order2.place(CardPayment("4111222233334444", card_limit=10000))   # limit too low
    order2.place(CardPayment("5555666677778888", card_limit=50000))   # works
    order2.print_bill()

    print()
    print("Phone stock before cancel:", phone.get_stock())
    order2.cancel()
    print("Phone stock after cancel :", phone.get_stock())
    order2.ship()                               # cannot ship a cancelled order

    # ---- Order history ----
    priya.show_order_history()
    arun.show_order_history()


if __name__ == "__main__":
    main()
