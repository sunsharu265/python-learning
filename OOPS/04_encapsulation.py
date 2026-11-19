"""
LESSON 4: ENCAPSULATION  (protecting the data)
==============================================

REAL LIFE IDEA
--------------
Think about an ATM.

    - Your money is locked INSIDE the machine.
    - You cannot open the machine and take the cash.
    - You must use the buttons: check balance, withdraw, deposit.
    - The machine CHECKS the rules (PIN correct? enough balance?).

Encapsulation = keep the data safe inside the object, and allow
changes only through methods that check the rules.

Another example: a medicine CAPSULE. The medicine is covered and
protected inside. That is where the word "encapsulation" comes from.

PYTHON NAMING RULES
-------------------
    name      -> public    : anyone can use it
    _name     -> protected : "please do not touch from outside" (a polite request)
    __name    -> private   : Python hides it from outside the class
"""


# ---------------------------------------------------------------
# Example 1: The problem WITHOUT encapsulation
# ---------------------------------------------------------------
class UnsafeAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


unsafe = UnsafeAccount("Ravi", 1000)
unsafe.balance = -50000          # Nobody stops this. Wrong data!
print("Unsafe balance:", unsafe.balance)


# ---------------------------------------------------------------
# Example 2: The solution WITH encapsulation
# ---------------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance         # two underscores = private

    # "Getter": a safe way to READ the private value.
    def get_balance(self):
        return self.__balance

    # Methods are the only doors to change the balance, and they check rules.
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be more than 0.")
            return
        self.__balance += amount
        print(f"Deposited Rs.{amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance.")
            return
        self.__balance -= amount
        print(f"Withdrew Rs.{amount}")


account = BankAccount("Meena", 1000)
account.deposit(500)
account.withdraw(5000)           # rule stops this
account.deposit(-100)            # rule stops this
print("Balance:", account.get_balance())

# print(account.__balance)       # ERROR if you remove the #  -> it is hidden


# ---------------------------------------------------------------
# Example 3: Getter and setter with a rule
# ---------------------------------------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.set_marks(marks)            # use the setter so the rule applies

    def get_marks(self):
        return self.__marks

    # "Setter": a safe way to CHANGE the private value.
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print(f"Invalid marks {marks}. Marks must be between 0 and 100.")


student = Student("Priya", 85)
student.set_marks(150)           # rejected
student.set_marks(92)            # accepted
print(student.name, "scored", student.get_marks())


# ---------------------------------------------------------------
# Example 4 (extra): the Python shortcut - @property
# ---------------------------------------------------------------
# @property lets us use a getter like a normal attribute (no brackets).
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):                 # getter
        return self.__price

    @price.setter
    def price(self, new_price):      # setter
        if new_price < 0:
            print("Price cannot be negative.")
        else:
            self.__price = new_price


pen = Product("Pen", 10)
pen.price = -5                   # the setter runs and rejects it
pen.price = 12                   # the setter runs and accepts it
print(pen.name, "costs Rs.", pen.price)


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create a class "Person" with a private __age. Add get_age() and
#    set_age(age). The setter must reject ages below 0 or above 120.
#
# 2. Create a class "WaterTank" with capacity (litres) and a private
#    __level starting at 0. Add fill(litres) - it must not go above the
#    capacity - and use(litres) - it must not go below 0. Add get_level().
#
# 3. Create a class "Locker" with a private __pin and private __item.
#    Add open(pin) which returns the item only when the pin is correct,
#    otherwise prints "Wrong PIN".
#
# 4. Create a class "MobileRecharge" with a private __balance.
#    Add recharge(amount) (only 10 to 5000 allowed) and
#    make_call(minutes) which costs Rs.1 per minute and must not allow
#    a call when the balance is too low.
#
# 5. Rewrite assignment 1 using @property instead of get_age/set_age.
