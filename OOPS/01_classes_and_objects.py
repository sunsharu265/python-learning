"""
LESSON 1: CLASSES AND OBJECTS
=============================

REAL LIFE IDEA
--------------
Think about a COOKIE CUTTER and COOKIES.

    Cookie cutter  ->  the shape / design      ->  CLASS
    Cookies        ->  the real things we eat  ->  OBJECTS

One cutter can make many cookies. Every cookie has the same shape,
but each one can have a different colour or topping.

More examples:
    Class (design)        Objects (real things)
    --------------        ---------------------
    Student               Priya, Arun, Meena
    Car                   my red Swift, your white Innova
    Mobile Phone          my phone, your phone

A CLASS has two kinds of things inside it:
    1. ATTRIBUTES -> what the object HAS   (name, age, colour)   = variables
    2. METHODS    -> what the object DOES  (study, drive, call)  = functions
"""


# ---------------------------------------------------------------
# Example 1: The smallest possible class
# ---------------------------------------------------------------
# "class" keyword creates a class. Class names start with a Capital letter.
class Dog:
    # A method is just a function written inside a class.
    # Every method gets "self" as its first parameter (explained in Lesson 2).
    def bark(self):
        print("Woof! Woof!")


# Creating an object = calling the class like a function.
my_dog = Dog()
my_dog.bark()          # object.method()


# ---------------------------------------------------------------
# Example 2: One class, many objects
# ---------------------------------------------------------------
class Student:
    def study(self):
        print("I am studying Python.")

    def play(self):
        print("I am playing badminton.")


student1 = Student()   # first object
student2 = Student()   # second object
newStudent = Student()   # third object
student1.study()
student2.play()


# Both are Student objects, but they are two DIFFERENT objects.
print(type(student2))            # <class '__main__.Student'>
print(student1 == student2)      # False -> two separate cookies


# ---------------------------------------------------------------
# Example 3: Giving an object its own data
# ---------------------------------------------------------------
class Car:
    def start(self):
        print("The car has started.")


car1 = Car()
car2 = Car()

# We can attach data to an object using the dot.
car1.colour = "Red"
car2.colour = "White"

print("Car 1 colour:", car1.colour)
print("Car 2 colour:", car2.colour)
car1.start()

# NOTE: Adding attributes like this works, but it is not the best way.
# In Lesson 2 we learn the proper way: the constructor (__init__).


# ===============================================================
# PRACTICE ASSIGNMENTS  (write your code below each question)
# ===============================================================
# 1. Create a class "Cat" with a method meow() that prints "Meow!".
#    Create one Cat object and call meow().
#
# 2. Create a class "Fan" with two methods: switch_on() and switch_off().
#    Each one prints a message. Create an object and call both.
#
# 3. Create a class "Teacher" with a method teach() that prints
#    "I am teaching Maths." Create THREE teacher objects and call
#    teach() on each of them.
#
# 4. Create a class "Phone". Create two objects. Give the first one
#    brand = "Samsung" and the second one brand = "Apple" (like car1.colour).
#    Print both brands.
#
# 5. THINK AND WRITE (no code): Look around your home. Write 5 classes
#    you can see, and for each one write 2 attributes and 2 methods.
#    Example:  Class: TV | Attributes: brand, size | Methods: turn_on, change_channel
