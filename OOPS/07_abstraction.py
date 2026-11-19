"""
LESSON 7: ABSTRACTION  (show what it does, hide how it does it)
===============================================================

REAL LIFE IDEA
--------------
    TV remote : you press the "volume +" button. You do not know
                (or care) what happens on the circuit board inside.
    Car       : you press the accelerator. You do not need to know
                how the engine burns fuel.
    UPI app   : you tap "Pay". The bank work behind it is hidden.

Abstraction = give a simple set of buttons; hide the difficult part.

THE RULE BOOK (abstract class)
------------------------------
An abstract class is a RULE BOOK for its children. It says:
    "Every child MUST have these methods."
It does not say how. Each child writes its own "how".

    - We cannot create an object from an abstract class.
    - A child that forgets a required method also cannot be created.

Real life: a government form says every shop MUST have a licence
number and a bill book. Each shop arranges it in its own way.
"""

from abc import ABC, abstractmethod      # ABC = Abstract Base Class


# ---------------------------------------------------------------
# Example 1: A rule book for payments
# ---------------------------------------------------------------
class Payment(ABC):                      # inherit from ABC = rule book
    @abstractmethod
    def pay(self, amount):               # rule: every payment must have pay()
        pass                             # no body here - children write it


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} in cash.")


class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI ({self.upi_id}).")


class CardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        last_four = self.card_number[-4:]
        print(f"Paid Rs.{amount} using card ending with {last_four}.")


# The shopkeeper only says "pay". The details stay hidden in each class.
def checkout(payment, amount):
    payment.pay(amount)


checkout(CashPayment(), 250)
checkout(UPIPayment("priya@upi"), 1200)
checkout(CardPayment("1234567812345678"), 5000)

# payment = Payment()        # ERROR if you remove the # -> rule book only


# ---------------------------------------------------------------
# Example 2: What happens when a child breaks the rule
# ---------------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    # An abstract class CAN also have normal methods that children reuse.
    def describe(self):
        print(f"I am a {type(self).__name__} with area {self.area():.2f}")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class BrokenShape(Shape):
    pass                                 # forgot to write area()


Square(5).describe()

try:
    BrokenShape()
except TypeError as error:
    print("Python stopped us:", error)


# ---------------------------------------------------------------
# Example 3: Hiding difficult steps behind one simple method
# ---------------------------------------------------------------
class CoffeeMachine:
    def make_coffee(self):               # the ONE button the user presses
        self.__boil_water()
        self.__add_coffee_powder()
        self.__add_milk_and_sugar()
        print("Your coffee is ready!")

    # Private helper methods: the hidden inside work.
    def __boil_water(self):
        print("  (boiling water...)")

    def __add_coffee_powder(self):
        print("  (adding coffee powder...)")

    def __add_milk_and_sugar(self):
        print("  (adding milk and sugar...)")


machine = CoffeeMachine()
machine.make_coffee()


# ---------------------------------------------------------------
# ENCAPSULATION vs ABSTRACTION (students often mix these up)
# ---------------------------------------------------------------
# Encapsulation : PROTECT the data      (ATM locks your money inside)
# Abstraction   : HIDE the difficulty   (ATM shows only simple buttons)


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create an abstract class "Animal" with an abstract method sound().
#    Create "Dog", "Cat" and "Lion" that write their own sound().
#
# 2. Create an abstract class "Vehicle" with abstract methods start()
#    and stop(). Create "Bike" and "Bus". Try to create Vehicle()
#    inside try/except and print the error.
#
# 3. Add "Rectangle" and "Circle" children for the Shape class above.
#    Call describe() on each one.
#
# 4. Create an abstract class "Notification" with abstract method
#    send(message). Create "SMSNotification", "EmailNotification" and
#    "WhatsAppNotification". Write a function notify_all(list, message)
#    that sends the message through every one.
#
# 5. Create a class "WashingMachine" with one public method wash()
#    that calls private steps: fill water, wash, rinse, dry.
