"""
LESSON 2: CONSTRUCTOR (__init__) AND self
=========================================

REAL LIFE IDEA
--------------
When a baby is born, the hospital fills a form IMMEDIATELY:
name, date of birth, weight. Nobody waits for one year to fill it.

In the same way, when an object is "born", Python runs a special
method called __init__ automatically. We use it to fill in the
object's starting details.

    __init__  = the "birth form" of the object  (called the CONSTRUCTOR)
    self      = "this object itself" (me / my)

Read  self.name = name  as:  "MY name is the name you gave me".
"""


# ---------------------------------------------------------------
# Example 1: A class with a constructor
# ---------------------------------------------------------------
class Student:
    # __init__ has TWO underscores on each side.
    # It runs automatically when we write Student(...).
    def __init__(self, name, age):
        self.name = name      # self.name -> stored inside the object
        self.age = age        # name, age -> values the caller gave

    def introduce(self):
        # Methods use self to read the object's own data.
        print(f"Hi, I am {self.name} and I am {self.age} years old.")


# We give name and age. We do NOT give self - Python gives it for us.
student1 = Student("Priya", 20)
student2 = Student("Arun", 22)

student1.introduce()     # self = student1
student2.introduce()     # self = student2

print(student1.name)     # we can read attributes with the dot
student1.age = 21        # ...and change them
student1.introduce()


# ---------------------------------------------------------------
# Example 2: Default values in the constructor
# ---------------------------------------------------------------
# Same idea as default parameters in functions (see functions.py).
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited Rs.{amount}. Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Sorry {self.owner}, not enough balance.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew Rs.{amount}. Balance: Rs.{self.balance}")


account1 = BankAccount("Meena")           # balance uses default 0
account2 = BankAccount("Ravi", 5000)      # balance is 5000

account1.deposit(1000)
account2.withdraw(2000)
account1.withdraw(5000)                   # not enough balance

# Each object keeps its OWN data. Meena's balance does not touch Ravi's.
print("Meena:", account1.balance)
print("Ravi :", account2.balance)


# ---------------------------------------------------------------
# Example 3: Methods can return values and use other attributes
# ---------------------------------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


room = Rectangle(10, 5)
print("Area of room:", room.area())
print("Perimeter of room:", room.perimeter())


# ---------------------------------------------------------------
# COMMON MISTAKES
# ---------------------------------------------------------------
# 1. Forgetting self in the method:      def introduce():        -> error
# 2. Forgetting self. before the name:   print(name)             -> error
# 3. Writing _init_ with ONE underscore: it will never run.
# 4. Forgetting the values:              Student()               -> error


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create a class "Book" with title, author and price in __init__.
#    Add a method show_details() that prints all three.
#    Create 2 books and call show_details() on both.
#
# 2. Create a class "Circle" with radius. Add methods area() and
#    circumference() that RETURN the values (use pi = 3.14159).
#
# 3. Create a class "Employee" with name and monthly_salary.
#    Add a method yearly_salary() that returns monthly_salary * 12.
#    Add a method give_raise(amount) that increases the monthly salary.
#
# 4. Create a class "MobilePhone" with brand, model and battery=100
#    (default). Add a method use(minutes) that reduces battery by
#    1 for every 10 minutes, and a method charge() that sets it to 100.
#
# 5. Create a class "Student" with name and three marks
#    (tamil, english, maths). Add methods total(), average() and
#    result() which returns "Pass" if every mark is 35 or more,
#    otherwise "Fail".
