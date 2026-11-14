# Menu: a list of dictionaries. Each dictionary is one item with its price.
MENU = [
    {"item": "2 Dosa", "price": 30},
    {"item": "2 Idli", "price": 20},
    {"item": "2 Poori", "price": 30},
    {"item": "Pongal", "price": 50},
    {"item": "Parotta", "price": 40},
    {"item": "Chappathi", "price": 50},
    {"item": "Vada", "price": 10},
]


# hotel_name is an OPTIONAL parameter: if the caller gives nothing,
# Python uses the default value written after the "=" sign.
def greet(hotel_name="Sharulatha Hotel"):
    print(f"Welcome to {hotel_name}. We are happy to serve you.")


def get_customer_details():
    name = input("Enter customer name: ")
    contact = input("Enter contact number: ")
    return name, contact


def show_menu():
    print("\n--- Menu ---")
    number = 1
    for menu_item in MENU:
        print(f"{number}. {menu_item['item']} - Rs.{menu_item['price']}")
        number += 1


def get_customer_order():
    order_items = []
    
    while True:
        choice = input("Enter item number (or 'done' to finish): ")
        if choice.lower() == 'done':
            break

        number = int(choice)
        if number < 1 or number > len(MENU):
            print("Sorry, that number is not on the menu.")

        # List positions start at 0, so item number 1 is MENU[0].
        order_items.append(MENU[number - 1])

    return order_items


def generate_bill(order_items):
    total_a  mount = 0
    print("\n--- Bill ---")

    for item in order_items:
        print(f"{item['item']}: Rs.{item['price']:.2f}")
        total_amount += item['price']

    print(f"Subtotal: Rs.{total_amount:.2f}")
    return total_amount


# tax_rate is OPTIONAL: calculate_total_with_tax(100) uses 5%,
# calculate_total_with_tax(100, 12) uses 12%.
def calculate_total_with_tax(amount, tax_rate=5):
    tax_amount = amount * tax_rate / 100
    final_total = amount + tax_amount
    return final_total


def main():
    greet()  # Call greet() with the default hotel name
    # greet('Kishore Hotel')  # Call greet() with a specific hotel name
    name, contact = get_customer_details()
    show_menu()
    order = get_customer_order()
    subtotal = generate_bill(order)
    
    tax_input = input("Enter tax rate % (press Enter for default 5%): ")
    if tax_input == "":
        final_total = calculate_total_with_tax(subtotal)  # default used
    else:
        final_total = calculate_total_with_tax(subtotal, float(tax_input))

    print(f"\nCustomer: {name}")
    print(f"Contact: {contact}")
    print(f"Tax Amount: Rs.{final_total - subtotal:.2f}")
    print(f"Final Total: Rs.{final_total:.2f}")


if __name__ == "__main__":
    main()
