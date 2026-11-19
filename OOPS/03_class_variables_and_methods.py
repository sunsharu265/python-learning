"""
LESSON 3: INSTANCE VARIABLES vs CLASS VARIABLES
===============================================

REAL LIFE IDEA
--------------
Think about students in ONE school.

    School name   -> SAME for every student       -> CLASS variable
    Student name  -> DIFFERENT for every student  -> INSTANCE variable

If the school changes its name, it changes for everybody at once.
If Priya changes her name, only Priya's name changes.

    Instance variable : written inside __init__ with self.   (one per object)
    Class variable    : written directly inside the class.   (shared by all)
"""


# ---------------------------------------------------------------
# Example 1: Shared data with a class variable
# ---------------------------------------------------------------
class Student:
    school_name = "Government High School"     # CLASS variable (shared)

    def __init__(self, name, standard):
        self.name = name                       # INSTANCE variables (own)
        self.standard = standard

    def show(self):
        print(f"{self.name}, Std {self.standard}, {Student.school_name}")


s1 = Student("Priya", 10)
s2 = Student("Arun", 9)
s1.show()
s2.show()

# Change the class variable using the CLASS name -> changes for everyone.
Student.school_name = "Model Higher Secondary School"
s1.show()
s2.show()


# ---------------------------------------------------------------
# Example 2: Counting how many objects were created
# ---------------------------------------------------------------
class Customer:
    total_customers = 0                # shared counter

    def __init__(self, name):
        self.name = name
        Customer.total_customers += 1  # every new customer adds 1


Customer("Meena")
Customer("Ravi")
Customer("Lakshmi")
print("Total customers:", Customer.total_customers)   # 3


# ---------------------------------------------------------------
# Example 3: A shared setting used in calculations
# ---------------------------------------------------------------
class HotelBill:
    tax_percent = 5                    # same tax for every bill

    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount

    def final_amount(self):
        tax = self.amount * HotelBill.tax_percent / 100
        return self.amount + tax


bill1 = HotelBill("Kishore", 200)
bill2 = HotelBill("Sharulatha", 400)
print(bill1.customer_name, "pays Rs.", bill1.final_amount())
print(bill2.customer_name, "pays Rs.", bill2.final_amount())

HotelBill.tax_percent = 12             # government changed the tax
print("After tax change:", bill1.final_amount(), bill2.final_amount())


# ---------------------------------------------------------------
# Example 4 (extra): class methods and static methods
# ---------------------------------------------------------------
# Normal method  -> works with ONE object      -> first parameter: self
# @classmethod   -> works with the CLASS       -> first parameter: cls
# @staticmethod  -> a helper; needs neither self nor cls
class Pizza:
    shop_name = "Pizza Corner"

    def __init__(self, size, price):
        self.size = size
        self.price = price

    def describe(self):                       # normal method
        print(f"{self.size} pizza - Rs.{self.price}")

    @classmethod
    def change_shop_name(cls, new_name):      # changes shared data
        cls.shop_name = new_name

    @staticmethod
    def is_valid_size(size):                  # simple helper
        return size in ["Small", "Medium", "Large"]


pizza = Pizza("Medium", 250)
pizza.describe()
Pizza.change_shop_name("Royal Pizza")
print(Pizza.shop_name)
print(Pizza.is_valid_size("Large"))      # True
print(Pizza.is_valid_size("Giant"))      # False


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create a class "Employee" with a class variable
#    company_name = "ABC Pvt Ltd" and instance variables name and salary.
#    Create 3 employees and print their name with the company name.
#    Then change the company name and print again.
#
# 2. Create a class "Car" with a class variable wheels = 4.
#    Create 2 cars with different brands and print the brand and wheels.
#
# 3. Create a class "Book" that counts how many books were created
#    (like Customer.total_customers). Create 4 books and print the count.
#
# 4. Create a class "SavingsAccount" with a class variable
#    interest_rate = 4 and instance variables owner and balance.
#    Add a method yearly_interest() that returns balance * interest_rate / 100.
#    Change interest_rate to 6 and show the new interest for every account.
#
# 5. THINK AND WRITE: For a class "Player" in a cricket team, write
#    which of these are class variables and which are instance variables:
#    team_name, player_name, jersey_number, coach_name, runs_scored.
