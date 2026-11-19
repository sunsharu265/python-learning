# supermarket
#  Practice Questions
# 1. Write an if/elif/else statement that prints "Freezing", "Mild", or "Warm" based on a temperature value.
# 2. Use a for loop to print every item in the list ["red", "green", "blue"].
# 3. Write a while loop that counts down from 10 to 1 and prints each number.
# 4. Create a loop that skips the number 3 using continue, and stops when a value reaches 10 using break.
# 5. Explain why indentation is required in Python control flow statements.
# 6. Challenge: Use a nested if inside a for loop to print only numbers greater than 5 from the range 1 to 10.


def great(supermarket_KS):
    print(f'Welcome to {supermarket_KS}:we are happyto help you to find your products')

    MENU =[
        {"item":"1KG rice","price": 500},
        {"item":"1kg dall","price": 600},
        {"item":"1kg sugar","price":400},
        {"item":"1kg  salt","price":200},
        {"item":"1kg oil","price" :700},
        ]
def get_customer_details():
    name = input("enter your name:")
    contact = input("enter your contact number:")
    return name, contact
def display_menu(MENU):
    print("Available items in the supermarket:")
    for item in MENU:
        print(f"{item['item']} - Price: {item['price']}")
def get_customer_order(MENU):
    order = []
    while True:
        item_name = input("Enter the item you want to order (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        for item in MENU:
            if item['item'].lower() == item_name.lower():
                order.append(item)
                print(f"Added {item['item']} to your order.")
                break
        else:
            print("Item not found. Please try again.")
    return order        
def generate_bill(order_items):
    total_amount = 0
    print("\n--- Bill ---")
    for item in order_items:
        print(f"{item['item']}: Rs.{item['price']:.2f}")
        total_amount += item['price']
    print(f"Subtotal: Rs.{total_amount:.2f}")
    return total_amount
def calculate_total_with_tax(amount, tax_rate=5):
    tax_amount = amount * tax_rate / 100
    final_total = amount + tax_amount
    return final_total
def main():
    great("KS Supermarket")  # Call greet() with the default supermarket name
    name, contact = get_customer_details()
   
    display_menu(MENU)
    order_items = get_customer_order(MENU)
    subtotal = generate_bill(order_items)
    final_total = calculate_total_with_tax(subtotal)
    tax_input=input("Enter tax rate (or press Enter to use default 5%): ")
    
    if tax_input== "":
        final_total = calculate_total_with_tax(subtotal)
    else:
        tax_rate = float(tax_input)
        final_total = calculate_total_with_tax(subtotal, tax_rate)   

    print(f"Customer Name: {name}")
    print(f"Contact: {contact}")
    print(f"Tax Amount: Rs.{final_total - subtotal:.2f}")
    print(f"Final Total: Rs.{final_total:.2f}")
    