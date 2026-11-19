"""
LESSON 8: SPECIAL METHODS  (also called "magic" or "dunder" methods)
====================================================================

REAL LIFE IDEA
--------------
Special methods have two underscores on both sides: __init__, __str__ ...
("dunder" = Double UNDERscore). We never call them directly.
Python calls them FOR us at the right moment.

    We write            Python secretly calls
    -----------         ---------------------
    Student("Priya")    __init__
    print(student)      __str__
    len(cart)           __len__
    a == b              __eq__
    a + b               __add__
    a < b               __lt__

It is like teaching your class to understand the normal Python signs.
"""


# ---------------------------------------------------------------
# Example 1: __str__ - a nice text when we print the object
# ---------------------------------------------------------------
class PlainBook:
    def __init__(self, title):
        self.title = title


print(PlainBook("Ponniyin Selvan"))      # ugly: <__main__.PlainBook object at 0x...>


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):                   # must RETURN text, not print it
        return f"'{self.title}' by {self.author} - Rs.{self.price}"


book = Book("Ponniyin Selvan", "Kalki", 450)
print(book)                              # nice!


# ---------------------------------------------------------------
# Example 2: __eq__ - deciding when two objects are "equal"
# ---------------------------------------------------------------
class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name

    def __eq__(self, other):
        # Two students are the same when the roll number is the same.
        return self.roll_number == other.roll_number


a = Student(101, "Priya")
b = Student(101, "Priya K")
c = Student(102, "Arun")
print(a == b)      # True  - same roll number
print(a == c)      # False


# ---------------------------------------------------------------
# Example 3: __len__ - making len() work on our object
# ---------------------------------------------------------------
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} songs"


playlist = Playlist("Morning Songs")
playlist.add_song("Song A")
playlist.add_song("Song B")
print(len(playlist))     # 2
print(playlist)


# ---------------------------------------------------------------
# Example 4: __add__ and __lt__ - making + and < work
# ---------------------------------------------------------------
class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __add__(self, other):            # money1 + money2
        return Money(self.rupees + other.rupees)

    def __lt__(self, other):             # money1 < money2
        return self.rupees < other.rupees

    def __str__(self):
        return f"Rs.{self.rupees}"


pocket = Money(500)
purse = Money(1200)
print(pocket + purse)        # Rs.1700
print(pocket < purse)        # True

# Because of __lt__, sorting and max() also work on our objects.
amounts = [Money(300), Money(50), Money(900)]
print("Biggest:", max(amounts))


# ===============================================================
# PRACTICE ASSIGNMENTS
# ===============================================================
# 1. Create a class "Movie" with title, year and rating. Add __str__
#    so that print(movie) shows:  Vikram (2022) - 8.3/10
#
# 2. Create a class "Product" with code and name. Add __eq__ so that
#    two products are equal when their code is the same.
#
# 3. Create a class "Classroom" with a list of student names.
#    Add add_student(name) and __len__ so that len(classroom) gives
#    the number of students.
#
# 4. Create a class "Distance" with km. Add __add__ so that
#    Distance(5) + Distance(7) gives a Distance of 12 km, and __str__
#    to print it as "12 km".
#
# 5. Create a class "Player" with name and score. Add __lt__ that
#    compares scores. Create 4 players, put them in a list and print
#    the player with the highest score using max().
