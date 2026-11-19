"""
LESSON 9: COMPOSITION  (objects made from other objects)
========================================================

REAL LIFE IDEA
--------------
A car is not "a kind of" engine. A car HAS an engine, HAS wheels,
HAS a music system. Big things are built from smaller things.

    IS-A   -> Inheritance  : A Dog IS-A Animal
    HAS-A  -> Composition  : A Car HAS-A Engine

More examples:
    A School HAS Students and Teachers.
    A Shopping Cart HAS Products.
    An Order HAS a Customer, a Cart and a Payment.

Real programs (like the eCommerce example in the ecommerce folder)
are mostly built this way: many small classes working together.
"""


# ---------------------------------------------------------------
# Example 1: A car HAS an engine
# ---------------------------------------------------------------
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def start(self):
        print(f"Engine ({self.horse_power} HP) started.")


class Car:
    def __init__(self, brand, horse_power):
        self.brand = brand
        self.engine = Engine(horse_power)    # the Car object owns an Engine object

    def start(self):
        print(f"{self.brand} key turned.")
        self.engine.start()                  # Car asks its Engine to do the work


car = Car("Maruti Swift", 88)
car.start()
print("Power:", car.engine.horse_power)      # object inside object: two dots


# ---------------------------------------------------------------
# Example 2: A person HAS an address
# ---------------------------------------------------------------
class Address:
    def __init__(self, street, city, pincode):
        self.street = street
        self.city = city
        self.pincode = pincode

    def __str__(self):
        return f"{self.street}, {self.city} - {self.pincode}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address               # an Address object given from outside


home = Address("12 Gandhi Street", "Coimbatore", "641001")
person = Person("Sharulatha", home)
print(f"{person.name} lives at {person.address}")
print("City only:", person.address.city)


# ---------------------------------------------------------------
# Example 3: A library HAS many books (a list of objects)
# ---------------------------------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []                      # list that will hold Book objects

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You borrowed '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def show_books(self):
        print(f"--- {self.name} ---")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title} by {book.author} [{status}]")


library = Library("City Library")
library.add_book(Book("Thirukkural", "Thiruvalluvar"))
library.add_book(Book("Wings of Fire", "A.P.J. Abdul Kalam"))

library.lend_book("Wings of Fire")
library.lend_book("Wings of Fire")           # already borrowed
library.show_books()


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create a class "Battery" (capacity) and a class "Phone" that HAS
#    a Battery. Add a method show() in Phone that prints the brand and
#    the battery capacity.
#
# 2. Create "Author" (name, country) and "Book" (title, author) where
#    author is an Author object. Print:  Wings of Fire by Kalam (India)
#
# 3. Create "Student" (name, marks) and "Classroom" that HAS a list of
#    students. Add add_student(), show_all() and topper() which returns
#    the student with the highest marks.
#
# 4. Create "Song" (title, minutes) and "Playlist" that HAS songs.
#    Add add_song() and total_minutes().
#
# 5. THINK AND WRITE: For each pair, write IS-A or HAS-A:
#    (Bus, Vehicle)  (Bus, Driver)  (House, Kitchen)  (Mango, Fruit)
#    (Hospital, Doctor)  (Doctor, Person)
