"""
LESSON 5: INHERITANCE  (child gets things from parent)
======================================================

REAL LIFE IDEA
--------------
A child gets things from the parents: surname, house, eye colour.
The child ALSO has their own new things (own hobby, own job).

In code:
    Parent class (base class)   -> has the common things
    Child class  (derived class)-> gets everything from the parent
                                   + adds its own things

Use the "IS-A" test to decide:
    A Dog IS-A Animal         -> Dog can inherit from Animal
    A Teacher IS-A Person     -> Teacher can inherit from Person
    A Car IS-A Engine  (no!)  -> do not use inheritance here

WHY? We write the common code only ONCE in the parent. No copy-paste.
"""


# ---------------------------------------------------------------
# Example 1: Basic inheritance
# ---------------------------------------------------------------
class Animal:                          # parent
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):                     # child: put the parent in brackets
    def bark(self):                    # Dog's own extra method
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")


dog = Dog("Tommy")
dog.eat()        # came from Animal
dog.sleep()      # came from Animal
dog.bark()       # Dog's own

cat = Cat("Kitty")
cat.eat()
cat.meow()
# cat.bark()     # ERROR: a Cat is not a Dog


# ---------------------------------------------------------------
# Example 2: super() - child adds its own attributes
# ---------------------------------------------------------------
# super() means "my parent". We call the parent's __init__ so that it
# sets the common attributes, then we add the new ones.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, standard):
        super().__init__(name, age)    # parent sets name and age
        self.standard = standard       # child adds standard

    def study(self):
        print(f"{self.name} studies in Std {self.standard}.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}.")


student = Student("Priya", 15, 10)
teacher = Teacher("Mrs. Lakshmi", 40, "Maths")

student.introduce()     # from Person
student.study()         # own
teacher.introduce()     # from Person
teacher.teach()         # own


# ---------------------------------------------------------------
# Example 3: Method overriding - child changes parent's behaviour
# ---------------------------------------------------------------
# If the child writes a method with the SAME name, the child's version wins.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_bonus(self):
        return self.salary * 0.10          # everyone gets 10%


class Manager(Employee):
    def yearly_bonus(self):                # OVERRIDE
        return self.salary * 0.20          # manager gets 20%


worker = Employee("Ravi", 20000)
manager = Manager("Meena", 50000)
print(worker.name, "bonus:", worker.yearly_bonus())
print(manager.name, "bonus:", manager.yearly_bonus())


# ---------------------------------------------------------------
# Example 4: Multi-level inheritance (grandparent -> parent -> child)
# ---------------------------------------------------------------
class Vehicle:
    def move(self):
        print("Vehicle is moving.")


class Car(Vehicle):
    def play_music(self):
        print("Car is playing music.")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging.")


tesla = ElectricCar()
tesla.move()          # from grandparent
tesla.play_music()    # from parent
tesla.charge()        # own

# Helpful checks
print(isinstance(tesla, Vehicle))      # True  - tesla IS-A Vehicle
print(issubclass(ElectricCar, Car))    # True


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create a parent class "Bird" with name and a method fly().
#    Create child classes "Parrot" (method talk()) and "Eagle"
#    (method hunt()). Create objects and call every method.
#
# 2. Create a parent class "Shape" with a method describe() that prints
#    "I am a shape". Create children "Square" (side) and "Circle" (radius),
#    each with its own area() method.
#
# 3. Create "Person" (name, phone). Create child "Doctor" that adds
#    specialisation, and child "Patient" that adds disease.
#    Use super().__init__() in both. Add a show() method in each child.
#
# 4. Create "Account" with owner, balance and a method
#    interest() returning balance * 3 / 100. Create "SavingsAccount"
#    that overrides interest() to give 5% and "FixedDeposit" that gives 7%.
#
# 5. Create three levels: "Device" (switch_on) -> "Phone" (call) ->
#    "SmartPhone" (take_photo). Create a SmartPhone and call all three.
