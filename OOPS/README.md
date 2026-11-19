# OOPS in Python - Beginner Lessons

**OOPS** = Object Oriented Programming System.
It means: we write programs by creating **objects**, the same way the real
world is made of objects (students, cars, phones, bank accounts).

## Lessons (follow this order)

| # | File | Concept | Real life example |
|---|------|---------|-------------------|
| 1 | `01_classes_and_objects.py` | Class and object | Cookie cutter and cookies |
| 2 | `02_constructor_and_self.py` | `__init__` and `self` | Birth form filled at the hospital |
| 3 | `03_class_variables_and_methods.py` | Instance vs class variables | School name vs student name |
| 4 | `04_encapsulation.py` | Encapsulation | ATM keeps your money locked inside |
| 5 | `05_inheritance.py` | Inheritance | Child gets things from parents |
| 6 | `06_polymorphism.py` | Polymorphism | Every animal "speaks" differently |
| 7 | `07_abstraction.py` | Abstraction | TV remote hides the circuits |
| 8 | `08_special_methods.py` | `__str__`, `__eq__`, `__len__` ... | Teaching your class to use `print`, `==`, `+` |
| 9 | `09_composition.py` | Composition (HAS-A) | A car has an engine |
| 10 | `ecommerce/` folder | Everything together | A small online shop |

## How to use each lesson

1. **Read** the top part of the file - it explains the idea with a real life example.
2. **Run** the file and match each line of output with the code:
   ```
   python OOPS/01_classes_and_objects.py
   ```
3. **Change** something small (a name, a number) and run it again.
4. **Do** the practice assignments at the bottom of the file.
   Write the answers in a new file, for example `OOPS/practice/lesson01.py`.

## The four pillars of OOPS (one line each)

| Pillar | Meaning | Remember it as |
|--------|---------|----------------|
| Encapsulation | Protect the data inside the object | ATM |
| Inheritance | Child class reuses the parent class | Family |
| Polymorphism | Same method name, different behaviour | Animals speaking |
| Abstraction | Show what it does, hide how | TV remote |

## Quick word list

| Word | Simple meaning |
|------|----------------|
| Class | The design / blueprint |
| Object | A real thing made from the class |
| Attribute | A variable inside an object (what it HAS) |
| Method | A function inside a class (what it DOES) |
| Constructor | `__init__` - runs when the object is created |
| `self` | "this object itself" |
| Parent / child class | The class that gives / the class that receives |
| Override | Child writes its own version of a parent's method |

## Final practice projects (after finishing all lessons)

Try to build one of these on your own. Each one needs 3 to 5 classes.

1. **Library system** - `Book`, `Member`, `Library`. Members borrow and return books;
   a member can hold at most 3 books.
2. **Hotel billing with classes** - rewrite `hotelBillingEx.py` using `MenuItem`,
   `Order` and `Bill` classes.
3. **School system** - `Person` -> `Student`, `Teacher`; `Classroom` has students
   and one teacher; print the topper and the class average.
4. **Bank system** - `Account` -> `SavingsAccount`, `CurrentAccount`; `Bank` has many
   accounts; deposit, withdraw and transfer between accounts.
5. **Bus ticket booking** - `Bus`, `Passenger`, `Ticket`; a bus has limited seats;
   child, adult and senior tickets have different prices.
