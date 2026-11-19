"""
LESSON 6: POLYMORPHISM  (same action, different behaviour)
==========================================================

REAL LIFE IDEA
--------------
"Poly" = many, "morph" = forms. One name, many forms.

    Ask every animal to "speak":
        Dog  -> Woof
        Cat  -> Meow
        Cow  -> Moo
    Same request ("speak"), different result for each one.

    One woman, many roles: at home she is a mother, in the office
    she is a manager, in a shop she is a customer. Same person,
    different behaviour depending on the place.

    The "+" sign:   2 + 3  -> 5        (adds numbers)
                  "a"+"b"  -> "ab"     (joins text)

WHY? We can write ONE piece of code that works for many types of
objects, without writing if/elif for every type.
"""


# ---------------------------------------------------------------
# Example 1: Polymorphism that Python already has
# ---------------------------------------------------------------
print(len("Python"))            # 6 letters
print(len([10, 20, 30]))        # 3 items
print(len({"a": 1, "b": 2}))    # 2 keys
# Same function len(), different kinds of things.


# ---------------------------------------------------------------
# Example 2: Same method name in different classes
# ---------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


class Cow(Animal):
    def speak(self):
        print(f"{self.name} says Moo!")


animals = [Dog("Tommy"), Cat("Kitty"), Cow("Lakshmi")]

# ONE loop. We do not check the type. Each object knows what to do.
for animal in animals:
    animal.speak()


# ---------------------------------------------------------------
# Example 3: One function that works with many shapes
# ---------------------------------------------------------------
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


def print_area(shape):
    # This function does not care WHICH shape it gets.
    # It only needs the shape to have an area() method.
    print(f"{type(shape).__name__} area = {shape.area():.2f}")


print_area(Square(4))
print_area(Rectangle(5, 3))
print_area(Circle(2))


# ---------------------------------------------------------------
# Example 4: Real use - different employees, different salary rules
# ---------------------------------------------------------------
class Employee:
    def __init__(self, name):
        self.name = name

    def monthly_pay(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def monthly_pay(self):
        return self.salary


class DailyWageWorker(Employee):
    def __init__(self, name, days_worked, pay_per_day):
        super().__init__(name)
        self.days_worked = days_worked
        self.pay_per_day = pay_per_day

    def monthly_pay(self):
        return self.days_worked * self.pay_per_day


staff = [
    FullTimeEmployee("Meena", 30000),
    DailyWageWorker("Ravi", 22, 700),
    FullTimeEmployee("Arun", 25000),
]

total = 0
for person in staff:
    pay = person.monthly_pay()          # same call, different calculation
    print(f"{person.name}: Rs.{pay}")
    total += pay
print("Total salary to pay: Rs.", total)


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create classes "Car", "Bike" and "Bus", each with a method
#    wheels() that prints how many wheels it has. Put one object of
#    each in a list and call wheels() in a loop.
#
# 2. Create a parent "Bird" with fly() printing "Bird can fly".
#    Create "Sparrow" (flies low), "Eagle" (flies high) and
#    "Penguin" (cannot fly) that override fly(). Call fly() in a loop.
#
# 3. Create "Triangle" (base, height) with an area() method and pass
#    it to the print_area() function above. It should work with no
#    change to print_area(). (This is the power of polymorphism!)
#
# 4. Create classes "Tamil", "English" and "Hindi", each with a
#    method greet() that prints hello in that language. Write ONE
#    function welcome(language) that calls language.greet().
#
# 5. Create a parent "Ticket" with price(). Create "ChildTicket"
#    (Rs.50), "AdultTicket" (Rs.120) and "SeniorTicket" (Rs.80).
#    A family buys 2 adult, 2 child and 1 senior ticket. Use a list
#    and a loop to print the total cost.
