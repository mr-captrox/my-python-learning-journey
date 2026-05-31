# ============================================================
#   🏗️  PYTHON OOP — Object-Oriented Programming
# ============================================================
#   Author  : Md Sourav Oyaj
#   Topics  : Classes & Objects · __init__ · self
#             Class vs Instance Attributes · Methods
#             __str__ · Inheritance · Polymorphism
#             Encapsulation · Operator Overloading
#             Inner / Nested Classes
#   Prerequisite: 01_python_basics.py
# ============================================================
#   WHY OOP?
#   Organizes code into "objects" that bundle data + behavior.
#   Real world: a Car has properties (brand, color) and
#   actions (drive, brake). OOP models this naturally.
# ============================================================


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 1 — CLASSES & OBJECTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A CLASS is a blueprint/template.
# An OBJECT is a specific instance created from that blueprint.
# Think: Class = "Cookie Cutter", Object = "Cookie"

class Employee:
    company = "HP"              # class attribute: shared by ALL instances

    def salary(self):           # method: a function inside a class
        return 34000

# Create objects (instances) from the class
e  = Employee()
e2 = Employee()

print(e.company,  e.salary())   # HP 34000
print(e2.company, e2.salary())  # HP 34000  ← both share company

# All objects from Employee share 'company'
print(Employee.company)         # HP  (access through class itself too)

# ── Naming conventions ────────────────────────────
# class name : CamelCase   → Employee, BankAccount
# method name: snake_case  → get_salary(), show_info()
# attribute  : snake_case  → self.name, self.dept

# ✅ TASK: Create a class "School" with a class attribute school_name.
#   Add a method get_name() that returns the school name.
#   Create 2 objects and call get_name() on both.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 2 — __init__  AND  self
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# __init__ is the CONSTRUCTOR — runs automatically when you
# create a new object. Used to set up the object's starting data.
#
# self  = the object itself. It links the method to the
#         specific object that called it.
# The name 'self' is a convention — you can use anything
# (as shown below with 'abc'), but 'self' is standard.

class Student:
    cgpa = 4.00             # ← class attribute (shared default)

    def __init__(self, name, dept, sem, cgpa):
        # These are INSTANCE attributes — unique per object
        self.name = name
        self.dept = dept
        self.sem  = sem
        self.cgpa = cgpa    # this SHADOWS the class attribute

    def get_name(self):
        return self.name

    def get_info(self):
        return (f"Name: {self.name} | Dept: {self.dept} | "
                f"Sem: {self.sem} | CGPA: {self.cgpa}")

# Create objects — parameters must match __init__
s  = Student("Md Sourav Oyaj", "CSE", 7, 3.0)
s2 = Student("Tanvir",         "CSE", 8, 3.5)

print(s.get_name())         # Md Sourav Oyaj
print(s2.get_info())        # Name: Tanvir | ...

s.get_info()                # returns string but nothing prints it here
print(s.get_info())         # ← need print() to show it

# ── class attribute vs instance attribute ─────────
print(s.cgpa)               # 3.0   ← instance attribute (specific to s)
print(Student.cgpa)         # 4.00  ← class attribute (original default)
# Instance attribute with same name SHADOWS the class attribute

# ── dir() shows all attributes and methods ─────────
print(dir(s))               # long list including dunder methods

# ── self parameter name demo ─────────────────────
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(abc):             # 'abc' instead of 'self' — still works!
        print(f"Hello, my name is {abc.name} and I am {abc.age}")

p1 = Person("John", 36)
p1.greet()                      # Hello, my name is John and I am 36
# ↑ Python automatically passes the object as the first argument

# ── Calling one method from another ──────────────
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello!, {self.name}"

    def welcome(self):
        msg = self.greet()              # calls greet() via self
        print(msg, "Welcome to our house!")

p1 = Greeter("Abhi")
p1.welcome()                    # Hello!, Abhi Welcome to our house!

# ✅ TASK 1: Create a "BankAccount" class with owner, balance in __init__.
#            Add method deposit(amount) and withdraw(amount) that update balance.
# ✅ TASK 2: Create a "Rectangle" class with width and height.
#            Add methods area() and perimeter().


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 3 — CLASS PROPERTIES (Add / Delete)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Class attribute shared across all objects ──────
class Person:
    lastname = ""               # class attribute, starts empty

    def __init__(self, name):
        self.name = name        # instance attribute

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"     # change it on the CLASS
print(p1.name, p1.lastname)     # Linus Refsnes
print(p2.name, p2.lastname)     # Emil Refsnes
# ↑ Both objects see the change because lastname is on the CLASS

# ── Adding a property to ONE specific object ──────
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Tobias")
p1.age  = 25                    # added only to p1, not to all Persons
p1.city = "Oslo"

print(p1.name)                  # Tobias
print(p1.age)                   # 25
print(p1.city)                  # Oslo
# p2.age would cause AttributeError if p2 existed without age

# ── Deleting a property ────────────────────────────
class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name  = name

    def show(self):
        print(self.brand, self.name)

c1 = Car("Ford", "Mustang")
del c1.name                     # delete the 'name' attribute
# c1.show()                     # ← AttributeError: 'Car' has no attribute 'name'
print(c1.brand)                 # Ford  (brand still exists)

# ── hasattr() — safely check if attribute exists ──
print(hasattr(c1, 'brand'))     # True
print(hasattr(c1, 'name'))      # False  (we deleted it)

# ✅ TASK: Create a Scoreboard class with a class attribute high_score = 0.
#   Create 3 objects with different scores.
#   Update high_score on the class if any object's score beats it.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 4 — __str__  METHOD  (String Representation)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# __str__ controls what print(object) shows.
# Without it, print gives ugly: <__main__.Person object at 0x...>

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __str__(self):
        return f"{self.name} ({self.age})"      # human-readable output

p1 = Person("Emil", 36)
print(p1)                   # Emil (36)   ← uses __str__
print(str(p1))              # Emil (36)

# Without __str__ you'd see: <__main__.Person object at 0x7f...>

# Another example
class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

b1 = Book("Clean Code", "Robert Martin", 431)
b2 = Book("Python Crash Course", "Eric Matthes", 540)
print(b1)       # 'Clean Code' by Robert Martin (431 pages)
print(b2)

# ✅ TASK: Add __str__ to your Rectangle class from Section 2.
#   It should return "Rectangle: 5×3  area=15".


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 5 — INHERITANCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Inheritance lets a child class get all the properties
# and methods of a parent class — and add its own.
# Syntax: class Child(Parent):

# ── Basic inheritance ─────────────────────────────
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    pass                        # 'pass' means "inherit everything, add nothing"

d1 = Dog("Rex")
d1.speak()                      # Rex  ← Dog uses Animal's speak()

# ── super() — call the parent's method ───────────
class Animal2:
    def __init__(self):
        pass

    def speak(self):
        print("Normal Animal Sound")

a = Animal2()
a.speak()                       # Normal Animal Sound

class Dog2(Animal2):
    def speak(self):
        super().speak()         # calls Animal2's speak() first
        print("Woof!")          # then adds its own

d = Dog2()
d.speak()
# Normal Animal Sound
# Woof!

# ── Inherit and extend __init__ ───────────────────
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname  = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)   # call Person's __init__
        self.gradyear = year             # add Student-specific attribute

    def welcome(self):
        print(f"Welcome, {self.firstname} {self.lastname} "
              f"to the class of {self.gradyear}!")

x = Student("Sourav", "Abhi", 2026)
x.welcome()     # Welcome, Sourav Abhi to the class of 2026!

# ── Multiple levels of inheritance ────────────────
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    def move(self):
        print("Drive")

class Boat(Vehicle):
    def move(self):
        print("Sail")

class Plane(Vehicle):
    def move(self):
        print("Fly")

car1   = Car("BMW",      "M5")
boat1  = Boat("Titanic", "Black")
plane1 = Plane("Airbus", "A380")

for obj in (car1, boat1, plane1):
    print(f"{obj.brand} {obj.model}", end=" → ")
    obj.move()

# ── isinstance() / issubclass() ──────────────────
print(isinstance(car1, Car))        # True
print(isinstance(car1, Vehicle))    # True   (Car IS-A Vehicle)
print(isinstance(car1, Boat))       # False
print(issubclass(Car, Vehicle))     # True

# ✅ TASK 1: Create a Shape base class with color and area() = 0.
#   Create Circle(Shape) and Triangle(Shape) that override area().
# ✅ TASK 2: Add a __str__ to each shape that prints its type and area.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 6 — POLYMORPHISM
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Poly = many, morph = forms.
# Same method name, different behavior depending on the class.
# "One interface, many implementations."

# ── Animals making different sounds ───────────────
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Cat(Animal):
    def speak(self):                # overrides Animal.speak
        print("Meow")

class Fox(Animal):
    def speak(self):                # overrides Animal.speak
        print("Wa-pa-pa-pa-pa-pow!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

c1 = Cat("Whiskers")
f1 = Fox("Foxy")
d1 = Dog("Rex")

# Polymorphism in action: same loop, different behavior!
for animal in (c1, f1, d1):
    animal.speak()              # each class prints differently

# ── Polymorphism with vehicles ─────────────────────
for obj in (Car("BMW","M5"), Boat("Titanic","Black"), Plane("Airbus","A380")):
    obj.move()                  # Drive / Sail / Fly

# ── Polymorphism with built-in functions ──────────
# Python's len() works on many types — that's polymorphism too!
print(len("hello"))             # 5   (string)
print(len([1, 2, 3]))           # 3   (list)
print(len({1, 2, 3, 4}))       # 4   (set)

# ── Duck typing ────────────────────────────────────
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't care about the class type — only if the method exists.
class Parrot:
    def speak(self):
        print("Polly wants a cracker!")

class Robot:
    def speak(self):
        print("BEEP BOOP. Hello human.")

for thing in (Parrot(), Robot(), Cat("Tom")):
    thing.speak()               # all have speak(), doesn't matter what class

# ✅ TASK: Create classes Circle, Square, Triangle each with
#   an area() method. Write a function print_area(shape) that
#   calls shape.area() — it works for all three!


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 7 — ENCAPSULATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Encapsulation = controlling access to an object's data.
# Prevents direct modification of sensitive attributes.
#
#  public    (no prefix)   → accessible anywhere       self.name
#  protected (_ prefix)    → convention: internal use  self._salary
#  private   (__ prefix)   → name-mangled, hidden      self.__age

# ── Private attribute (__ double underscore) ──────
class PersonPrivate:
    def __init__(self, name, age):
        self.nname  = name          # public
        self.__age  = age           # private (name-mangled)

    def get_age(self):
        return self.__age           # getter: controlled READ access

    def set_age(self, age):
        if age > 0:                 # validation!
            self.__age = age
        else:
            print("Age must be positive")

p1 = PersonPrivate("Sourav", 25)
print(p1.nname)                     # Sourav  ← public: works fine
# print(p1.age)                     # ← AttributeError: no 'age'
# print(p1.__age)                   # ← AttributeError: name-mangled
print(p1.get_age())                 # 25  ← controlled access via getter

p1.set_age(26)                      # ← setter validates before changing
print(p1.get_age())                 # 26

p1.set_age(-5)                      # "Age must be positive"
print(p1.get_age())                 # 26  (unchanged — validation worked)

# Note: Python doesn't truly block access (unlike Java).
# p1._PersonPrivate__age = 99       # hacky but technically works
# print(p1.get_age())               # 99

# ── Protected attribute (_ single underscore) ─────
# Just a convention — "don't touch this from outside, but you can"
class Worker:
    def __init__(self, name, salary):
        self.name    = name
        self._salary = salary           # protected

w1 = Worker("Linus", 50000)
print(w1.name)                          # Linus
print(w1._salary)                       # 50000  ← can access, but shouldn't
# ↑ No error, but convention says "don't do this directly"

# ── Scoreboard with private score ─────────────────
class Scoreboard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def add_points(self, pts):
        if pts > 0:
            self.__score += pts

s1 = Scoreboard(0)
print(s1.get_score())               # 0
s1.add_points(10)
print(s1.get_score())               # 10
# s1.__score = 9999                 # ← creates a NEW public __score, doesn't change private!

# ── @property decorator (Pythonic way) ────────────
# A cleaner way to write getters and setters
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):              # getter — access like an attribute
        return self.__celsius

    @celsius.setter
    def celsius(self, val):         # setter — validate on assignment
        if val < -273.15:
            print("Below absolute zero!")
        else:
            self.__celsius = val

    @property
    def fahrenheit(self):           # computed property (no setter needed)
        return self.__celsius * 9 / 5 + 32

t = Temperature(100)
print(t.celsius)                    # 100   ← looks like attribute access
print(t.fahrenheit)                 # 212.0
t.celsius = 0
print(t.fahrenheit)                 # 32.0
t.celsius = -300                    # "Below absolute zero!"

# ✅ TASK 1: Create a BankAccount class where balance is private.
#   Add deposit(), withdraw() (with "insufficient funds" check), and get_balance().
# ✅ TASK 2: Add @property to BankAccount so balance reads cleanly.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 8 — OPERATOR OVERLOADING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Define what +, -, *, == etc. mean for your own classes.
# Special "dunder" (double underscore) methods:
#   __add__  → +
#   __sub__  → -
#   __mul__  → *
#   __eq__   → ==
#   __lt__   → <

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(3, 5)
p2 = Point(3, 1)

result_sub = p1 - p2
print(result_sub.print_point())     # Point(0, 4)

result_add = p1 + p2
print(result_add)                   # (6, 6)  ← uses __str__

result_mul = p1 * 3
print(result_mul)                   # (9, 15)

print(p1 == p2)                     # False
print(p1 == Point(3, 5))            # True

# ── Another example: shopping cart ─────────────────
class CartItem:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        return f"{self.name}: ${self.price}"

item1 = CartItem("Book",  299)
item2 = CartItem("Pen",    49)
total = item1 + item2
print(f"Total: ${total}")           # Total: $348

# ✅ TASK: Create a Vector class with (x, y, z).
#   Overload +, - and write __str__ that shows "Vector(x, y, z)".


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 9 — INNER / NESTED CLASSES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A class defined inside another class.
# Useful for grouping related functionality,
# and hiding implementation details.

# ── Basic inner class ─────────────────────────────
# (Fixed from original code — original had broken usage)
class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self, outer_instance):
            self.name  = "Inner Class"
            self.outer = outer_instance     # store reference to outer

        def display(self):
            print(f"Hello from the {self.name}")
            print(f"Accessing outer: {self.outer.name}")   # reach outer!

# Step 1: create an outer instance
outer_obj = Outer()

# Step 2: create inner instance, passing the outer into it
inner_obj = Outer.Inner(outer_obj)

# Step 3: call the method
inner_obj.display()
# Hello from the Inner Class
# Accessing outer: Outer Class

# ── Why the original code had errors ──────────────
# outer1inner = outer.inner()       # ← missing 'outer_instance' arg → TypeError
# inner = outer.inner(outer)        # ← 'outer' is the class, not an instance!
# The correct pattern is shown above.

# ── Practical inner class example ─────────────────
class Library:
    library_name = "City Library"

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Library.Book(title, author)   # create an inner object
        self.books.append(book)
        print(f"Added: {book}")

    def list_books(self):
        print(f"\n{Library.library_name} — Catalogue:")
        for b in self.books:
            print(f"  {b}")

    class Book:                             # inner class
        def __init__(self, title, author):
            self.title  = title
            self.author = author

        def __str__(self):
            return f'"{self.title}" by {self.author}'

lib = Library()
lib.add_book("Clean Code",     "Robert Martin")
lib.add_book("Python Basics",  "Al Sweigart")
lib.list_books()

# Access the inner class directly (no outer instance needed for this)
standalone_book = Library.Book("The Pragmatic Programmer", "Hunt & Thomas")
print(standalone_book)

# ✅ TASK: Create a Company class with a class attribute company_name.
#   Inside it, create an Employee inner class with name and salary.
#   Company should have a method hire(name, salary) that creates an Employee
#   and stores it. Add list_employees() to print all employees.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 10 — PUTTING IT ALL TOGETHER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A full example that uses ALL OOP concepts together.

class Vehicle:
    """Base class for all vehicles."""
    total_vehicles = 0          # class attribute: counts all vehicles

    def __init__(self, brand, model):
        self.brand  = brand
        self.model  = model
        self.__fuel = 100       # private (encapsulation)
        Vehicle.total_vehicles += 1

    def move(self):
        print("Move!")

    def refuel(self, amount):
        if amount > 0:
            self.__fuel = min(100, self.__fuel + amount)

    @property
    def fuel(self):             # property (encapsulation)
        return self.__fuel

    def __str__(self):          # __str__
        return f"{self.brand} {self.model} (fuel: {self.__fuel}%)"


class Car(Vehicle):             # inheritance
    def __init__(self, brand, model, doors=4):
        super().__init__(brand, model)
        self.doors = doors

    def move(self):             # polymorphism — overrides Vehicle.move
        self.__fuel_use()
        print(f"{self.brand} {self.model} drives 🚗")

    def __fuel_use(self):       # private helper method
        pass                    # would decrease fuel in real app

    def __str__(self):
        return f"Car: {self.brand} {self.model} ({self.doors} doors)"


class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} sails ⛵")


class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} flies ✈")


# Create objects
car1   = Car("BMW",      "M5",     4)
car2   = Car("Tesla",    "Model S", 4)
boat1  = Boat("Yamaha",  "Wave Runner")
plane1 = Plane("Airbus", "A380")

print("─── All vehicles ───")
for v in (car1, car2, boat1, plane1):
    print(v)                    # uses __str__

print("\n─── Move! ───")
for v in (car1, car2, boat1, plane1):
    v.move()                    # polymorphism: each moves differently

print(f"\nTotal vehicles created: {Vehicle.total_vehicles}")

print("\n─── Check fuel ───")
print(f"{car1.brand} fuel: {car1.fuel}%")   # property (encapsulation)
car1.refuel(10)
print(f"After refuel: {car1.fuel}%")

# ✅ FINAL TASK:
# Build a simple "Animal Shelter" system:
#   1. Base class Animal(name, species, age) with __str__
#   2. Subclasses Dog and Cat that override a speak() method
#   3. Shelter class with a private __animals list
#   4. Shelter.admit(animal) to add an animal
#   5. Shelter.list_animals() to show all animals
#   6. Shelter.find(name) to find an animal by name
#   7. Create 3+ animals, admit them, list them, find one.


# ============================================================
#  END OF FILE 3 — PYTHON OOP
#  You now know: Basics + Collections + OOP — great journey!
# ============================================================
