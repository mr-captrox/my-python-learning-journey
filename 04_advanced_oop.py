# ============================================================
#   🏗️  ADVANCED OOP — Special Methods & Decorators
# ============================================================
#   Author  : Md Sourav Oyaj
#   Topics  : __repr__  vs  __str__
#             @staticmethod
#             @classmethod  (cls, change class variable)
#   Prerequisite: 03_python_oop.py
# ============================================================
#   HOW TO USE:
#   ▸ Open in VSCode → right-click → "Run in Interactive Window"
#   ▸ Each # %% block is one Jupyter cell — run them one by one
# ============================================================


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 1 — __str__  vs  __repr__
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Both control how your object is displayed as text.
# But they serve DIFFERENT audiences:
#
#  __str__   → for END USERS     — readable / friendly
#              called by print(), str()
#
#  __repr__  → for DEVELOPERS    — unambiguous / debuggable
#              called by repr(), in REPL, inside lists/dicts
#
# Golden rule: __repr__ should ideally show how to RE-CREATE
#              the object. __str__ just needs to look nice.

class Employee:
    company = "HP"              # class attribute — shared by all

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary    # ⚠️ BUG FIX: original had self.sslary (typo)

    # ── __str__: user-friendly output ─────────────
    def __str__(self):
        return (f"The name of the employee is {self.name} "
                f"and his salary is {self.salary}")

    # ── __repr__: developer/debug output ──────────
    def __repr__(self):
        return (f"Employee(name='{self.name}', salary={self.salary})")
        # ideally: enough info to recreate the object

    @staticmethod
    def calc_sum(a, b):
        return a + b

    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_comp):
        cls.company = new_comp


e1 = Employee("Ayan",   5000)
e2 = Employee("Sourav", 50000)

# ── str() / print() → uses __str__ ───────────────
print(str(e1))      # The name of the employee is Ayan and his salary is 5000
print(str(e2))      # The name of the employee is Sourav and his salary is 50000
print(e1)           # same as print(str(e1))

# ── repr() → uses __repr__ ───────────────────────
print(repr(e1))     # Employee(name='Ayan', salary=5000)
print(repr(e2))     # Employee(name='Sourav', salary=50000)

# ── Key difference in containers ──────────────────
# In a list, Python uses __repr__ for each item (not __str__)
employees = [e1, e2]
print(employees)
# [Employee(name='Ayan', salary=5000), Employee(name='Sourav', salary=50000)]
# ↑ repr is used here, not str!

# ── What happens with NO __str__ defined? ─────────
class Demo:
    def __repr__(self):
        return "Demo object — repr only"

d = Demo()
print(d)            # Demo object — repr only
# ↑ When __str__ is missing, Python falls back to __repr__
# So defining __repr__ is more important/fundamental.

# ── What happens with NO __repr__ either? ─────────
class Bare:
    pass

b = Bare()
print(b)            # <__main__.Bare object at 0x7f...>
print(repr(b))      # <__main__.Bare object at 0x7f...>
# ↑ the ugly default — always define at least __repr__

# ── Practical comparison side by side ─────────────
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):          # user sees: "(3, 5)"
        return f"({self.x}, {self.y})"

    def __repr__(self):         # dev sees: "Point(3, 5)"
        return f"Point({self.x}, {self.y})"

p = Point(3, 5)
print(str(p))       # (3, 5)      ← __str__
print(repr(p))      # Point(3, 5) ← __repr__
print(p)            # (3, 5)      ← print() uses __str__

# In a REPL (interactive terminal) typing just `p` uses __repr__
# In a list [p], __repr__ is used for each element

# ── Quick reference ───────────────────────────────
# +──────────────+───────────────+─────────────────────+
# │              │   __str__     │    __repr__          │
# +──────────────+───────────────+─────────────────────+
# │ Audience     │  End user     │  Developer/debug     │
# │ Triggered by │  print(), str │  repr(), REPL, lists │
# │ Goal         │  Readable     │  Unambiguous         │
# │ Fallback?    │  Yes → repr   │  No (shows address)  │
# +──────────────+───────────────+─────────────────────+

# ✅ TASK 1: Create a "Book" class with title, author, year.
#   __str__  → "Clean Code (Robert Martin, 2008)"
#   __repr__ → "Book('Clean Code', 'Robert Martin', 2008)"
# ✅ TASK 2: Put 3 Book objects in a list and print the list.
#            Notice which method is called automatically.
# ✅ TASK 3: What does Python show if you define only __repr__
#            and call print(obj)? Test it.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 2 — @staticmethod
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A static method belongs to the CLASS, not to any object.
# It does NOT receive 'self' (no instance) or 'cls' (no class).
# Use it for utility/helper functions that are logically related
# to the class but don't need to access instance or class data.

class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    @staticmethod
    def calc_sum(a, b):     # ← no self, no cls
        return a + b

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0   # helper: doesn't need the object

    @staticmethod
    def currency_format(amount):
        return f"${amount:,.2f}"

e1 = Employee("Ayan",   5000)
e2 = Employee("Sourav", 50000)

# ── Call via object OR directly via class ─────────
print(e1.calc_sum(3, 2))            # 5  — calling on instance
print(Employee.calc_sum(3, 2))      # 5  — calling on class directly
# Both work the same — no difference!

print(Employee.is_valid_salary(-100))       # False
print(Employee.is_valid_salary(5000))       # True
print(Employee.currency_format(e1.salary)) # $5,000.00

# ── When to use @staticmethod ─────────────────────
# ✔ The logic doesn't depend on the object's data (self)
# ✔ The logic doesn't depend on the class itself (cls)
# ✔ But it's still conceptually part of the class
# Example: a MathHelper class with static add(), subtract() methods

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

print(MathHelper.add(10, 20))          # 30
print(MathHelper.multiply(4, 5))       # 20
print(MathHelper.is_prime(17))         # True
print(MathHelper.is_prime(18))         # False

# ── Comparison: regular method vs static method ───
class Demo:
    val = 100

    def regular(self):          # needs an instance (self)
        return self.val         # can access instance data

    @staticmethod
    def static_one():           # needs NO instance
        return "I am static"   # cannot access self.val or cls.val

d = Demo()
print(d.regular())              # 100
print(d.static_one())           # I am static
print(Demo.static_one())        # I am static — no object needed!
# print(Demo.regular())         # ← TypeError: missing 'self'

# ✅ TASK 1: Add a @staticmethod validate_name(name) to Employee
#   that returns True only if name is a non-empty string.
# ✅ TASK 2: Create a "TemperatureConverter" class with only static methods:
#   celsius_to_fahrenheit(c), fahrenheit_to_celsius(f), celsius_to_kelvin(c).
# ✅ TASK 3: Can you call a @staticmethod without creating any object?
#   Test it and write your conclusion as a comment.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 3 — @classmethod
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A class method receives the CLASS itself as the first argument (cls).
# It CAN access and modify class-level data.
# Does NOT receive 'self' — not tied to a specific object.
# Use it to: read/change class attributes, or as alternative constructors.

class Employee:
    company = "HP"                  # class attribute (shared by all)

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def __str__(self):
        return (f"The name of the employee is {self.name} "
                f"and his salary is {self.salary}")

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

    @classmethod
    def print_company(cls):         # cls = Employee (the class)
        print(cls.company)

    @classmethod
    def change_company(cls, new_comp):
        cls.company = new_comp      # changes the class attribute for ALL

e1 = Employee("Ayan",   5000)
e2 = Employee("Sourav", 50000)

# ── Call via object OR class ───────────────────────
e1.print_company()          # HP
Employee.print_company()    # HP  (same result)

# ── Changing the class attribute affects ALL objects ─
print(e1.company)           # HP
print(e2.company)           # HP

e2.change_company("Apple")  # change via instance (still affects whole class)
print(e2.company)           # Apple
print(e1.company)           # Apple  ← e1 also changed! (same class var)
Employee.print_company()    # Apple

# ── @classmethod as alternative constructor ────────
# A powerful pattern: create objects from different input formats
class Student:
    def __init__(self, name, grade, age):
        self.name  = name
        self.grade = grade
        self.age   = age

    @classmethod
    def from_string(cls, data_str):
        """Create a Student from a string like 'Sourav-A-23'"""
        name, grade, age = data_str.split('-')
        return cls(name, grade, int(age))       # cls(...) = Student(...)

    @classmethod
    def from_dict(cls, data):
        """Create a Student from a dict"""
        return cls(data['name'], data['grade'], data['age'])

    def __str__(self):
        return f"{self.name} | Grade: {self.grade} | Age: {self.age}"

# Normal constructor
s1 = Student("Abhi", "A", 22)
print(s1)

# Alternative constructor from string (classmethod)
s2 = Student.from_string("Tanvir-B-21")
print(s2)

# Alternative constructor from dict (classmethod)
info = {'name': 'Reaz', 'grade': 'A+', 'age': 23}
s3 = Student.from_dict(info)
print(s3)

# ── Tracking instances with a class variable ───────
class Counter:
    count = 0                           # tracks how many objects created

    def __init__(self, name):
        self.name = name
        Counter.count += 1             # increment on every new object

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def reset(cls):
        cls.count = 0

c1 = Counter("First")
c2 = Counter("Second")
c3 = Counter("Third")
print(Counter.get_count())      # 3
Counter.reset()
print(Counter.get_count())      # 0

# ── Quick comparison: regular vs static vs class ───
# +─────────────+──────────────+──────────────+───────────────────────+
# │             │  1st param   │  Access self │  Access class (cls)   │
# +─────────────+──────────────+──────────────+───────────────────────+
# │ regular     │  self        │  ✅ Yes       │  via self.__class__   │
# │ @staticmethod│  (nothing)  │  ❌ No        │  ❌ No                │
# │ @classmethod │  cls        │  ❌ No        │  ✅ Yes               │
# +─────────────+──────────────+──────────────+───────────────────────+

class ShowAll:
    value = "class_value"

    def regular(self):
        return f"regular: self = {self}"

    @staticmethod
    def static():
        return "static: no self, no cls"

    @classmethod
    def class_m(cls):
        return f"classmethod: cls.value = {cls.value}"

obj = ShowAll()
print(obj.regular())        # regular: self = <__main__.ShowAll object...>
print(obj.static())         # static: no self, no cls
print(obj.class_m())        # classmethod: cls.value = class_value
print(ShowAll.static())     # works without object
print(ShowAll.class_m())    # works without object
# ShowAll.regular()         # ← TypeError: missing self

# ✅ TASK 1: Add a @classmethod employee_count(cls) that returns
#   how many Employee objects have been created. Use a class variable.
# ✅ TASK 2: Add a @classmethod from_csv(cls, csv_str) to Employee
#   that creates an object from "Sourav,50000".
# ✅ TASK 3: In which situation would you choose @classmethod over
#   @staticmethod? Write your answer as a comment.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 4 — FULL EMPLOYEE CLASS (All Together)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Combining __str__, __repr__, @staticmethod, @classmethod
# in one clean, well-organized class.

class Employee:
    company  = "HP"                 # class attribute
    _count   = 0                    # private: tracks total employees

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary        # ⚠️ was self.sslary in original (typo!)
        Employee._count += 1

    # ── Dunder methods ────────────────────────────
    def __str__(self):              # user-friendly
        return (f"The name of the employee is {self.name} "
                f"and his salary is {self.salary}")

    def __repr__(self):             # developer-friendly
        return f"Employee(name='{self.name}', salary={self.salary})"

    # ── Static methods ────────────────────────────
    @staticmethod
    def calc_sum(a, b):             # pure utility, no self/cls needed
        return a + b

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    # ── Class methods ─────────────────────────────
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_comp):
        cls.company = new_comp

    @classmethod
    def get_count(cls):
        return cls._count

    @classmethod
    def from_string(cls, data_str):     # alternative constructor
        name, salary = data_str.split(',')
        return cls(name, int(salary))

    # ── Regular method ────────────────────────────
    def give_raise(self, amount):
        if Employee.is_valid_salary(amount):
            self.salary += amount
            return f"{self.name}'s salary raised to {self.salary}"
        return "Invalid raise amount"


# ── Demo ──────────────────────────────────────────
e1 = Employee("Ayan",   5000)
e2 = Employee("Sourav", 50000)
e3 = Employee.from_string("Tanvir,35000")   # classmethod constructor

print("─── str() ───")
print(str(e1))
print(str(e2))

print("\n─── repr() ───")
print(repr(e2))
print(repr(e1))

print("\n─── static methods ───")
print(e1.calc_sum(3, 2))            # 5
print(Employee.calc_sum(10, 20))    # 30

print("\n─── class methods ───")
Employee.print_company()            # HP
e2.change_company("Apple")          # change for ALL
e2.print_company()                  # Apple
e1.print_company()                  # Apple ← e1 changed too!

print(f"\nTotal employees: {Employee.get_count()}")   # 3

print("\n─── regular method ───")
print(e1.give_raise(1000))          # Ayan's salary raised to 6000

print("\n─── in a list (uses repr) ───")
print([e1, e2, e3])


# ============================================================
#  END OF FILE 4 — ADVANCED OOP
#  Next: 05_advanced_functions.py  → raise · reduce · walrus · *args · **kwargs
# ============================================================
