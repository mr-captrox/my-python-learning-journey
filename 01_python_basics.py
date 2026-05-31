# ============================================================
#   🐍  PYTHON BASICS — Complete Beginner's Guide
# ============================================================
#   Author  : Md Sourav Oyaj
#   Topics  : Output · Variables · Types · Casting · Strings
#             Booleans · Operators · if/elif/else · match/case
#             While Loops · For Loops · Functions · Lambda
#             Recursion · Input · Try/Except · JSON · Math
# ============================================================
#   HOW TO USE:
#   ▸ Open in VSCode → right-click → "Run in Interactive Window"
#   ▸ Each # %% block is one Jupyter cell — run them one by one
# ============================================================


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 1 — HELLO WORLD & PRINT STATEMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# print() is the most basic function — it outputs text to the screen.

print("Hello, World!")          # classic first program
print("My name is Sourav")
print(100)                       # works with numbers too
print(3.14)
print(True)                      # and booleans

# --- Multiple values in one print ---
# By default, values are separated by a space
print("Name:", "Sourav", "Age:", 23)   # Name: Sourav Age: 23

# Custom separator with sep=
print("A", "B", "C", sep="-")         # A-B-C
print("2025", "01", "15", sep="/")     # 2025/01/15

# Custom line ending with end= (default is newline \n)
print("Hello", end=" ")                # stays on same line
print("World")                          # → Hello World

# Blank line
print()

# ✅ TASK 1: Print your name, city, and "I am learning Python!" on one line.
# ✅ TASK 2: Print "Dhaka-Bangladesh-Asia" using sep=.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 2 — VARIABLES & DATA TYPES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A variable is a named container for a value.
# Python figures out the data type automatically (dynamic typing).

# ── int : whole numbers ──────────────────────────
a = 2
print(a)            # 2
print(type(a))      # <class 'int'>

# ── str : text (use single or double quotes) ──────
b = "Hello, World!"
print(b)            # Hello, World!
print(type(b))      # <class 'str'>

# Variables can be re-assigned — even to a different type
b = 5
print(b)            # 5
print(type(b))      # <class 'int'>  ← type changed!

# Underscore _ is valid in variable names (but not hyphen -)
a_ = "Mhoro, Nyika!"       # valid ✓
# a-b = 5                  # SyntaxError ✗ (hyphen means subtraction)
print(a_)
print(type(a_))             # <class 'str'>

# ── float : decimal numbers ───────────────────────
pi = 3.14
print(pi)
print(type(pi))     # <class 'float'>

temp = -12.5
print(temp)

# ── bool : True or False (capital T and F!) ────────
is_fun   = True
is_hard  = False
print(is_fun)
print(type(is_fun))         # <class 'bool'>

# ── None : represents "no value / empty" ──────────
result = None
print(result)
print(type(result))         # <class 'NoneType'>

# ── Multiple assignment in one line ───────────────
name, age, city = "Sourav", 23, "Dhaka"
print(name, age, city)

# ── type() checks the type of any variable ─────────
print(type(a))              # <class 'int'>
print(type(b))              # <class 'int'>   (after reassignment)
print(type(a_))             # <class 'str'>

# ✅ TASK 1: Create variables: name (str), age (int), height (float), 
#            is_student (bool). Print each with its type().
# ✅ TASK 2: Assign three cities to three variables in ONE line, then print.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 3 — TYPE CASTING (Converting between types)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Use int(), float(), str(), bool() to convert types.

# float → int  (just cuts off the decimal, does NOT round)
c = int(3.14)
print(c)                    # 3
print(type(c))              # <class 'int'>

c2 = int(9.99)
print(c2)                   # 9  ← not 10! it truncates, not rounds

# int → str
d = str(12)
print(d)                    # "12"
print(d + "12")             # "1212"  ← string joining, not addition!
print(type(d))              # <class 'str'>

# str → int  (only works if the string looks like a number)
num_str = "50"
num_int = int(num_str)
print(num_int + 10)         # 60
# int("hello")              # ← ValueError: can't convert "hello" to int

# int / float → str
print(str(100) + " dollars")    # 100 dollars

# str → float
f = float("3.14")
print(f + 1)                # 4.140000000000001

# int → float
x = float(5)
print(x)                    # 5.0

# bool casts  (0, "", None, [] are False; everything else is True)
print(bool(0))              # False
print(bool(1))              # True
print(bool(""))             # False
print(bool("hello"))        # True

# round() — rounds to n decimal places
x = round(2.3243, 2)
print(x)                    # 2.32

x2 = round(43.32432, 1)
print(x2)                   # 43.3

x3 = round(2.5)             # no 2nd arg → rounds to nearest int
print(x3)                   # 2  (Python uses "banker's rounding")

# ✅ TASK 1: Convert the string "250" to int and multiply by 4.
# ✅ TASK 2: Round 3.14159265 to 4 decimal places.
# ✅ TASK 3: What happens when you do str(True)? Try it and check.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 4 — STRINGS (Deep Dive)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A string is a sequence of characters.
# String index starts at 0.

name = "Hello Sourav"

# ── Length ──────────────────────────────────────
print(len(name))            # 12  (spaces count too)

# ── Indexing  (0 = first, -1 = last) ────────────
print(name[0])              # H
print(name[6])              # S
print(name[-1])             # v  (last character)
print(name[-6])             # S  (6th from end)

# ── Slicing  [start : end]  (end NOT included) ───
myname = "sourav"
print(myname[0:2])          # so
print(myname[2:5])          # ura
print(myname[0:-1])         # soura  (everything except last char)
print(myname[-2:])          # av     (last 2 characters)
print(myname[:3])           # sou    (start is 0 by default)
# myname[-2:0] → ""         # ← empty! can't go backwards like this
print(myname[::2])          # sra    (every 2nd character — step)
print(myname[::-1])         # varuos (reverse the string!)

# ── Common String Methods ────────────────────────
astring = "Hello Sourav"
print(astring.index('S'))           # 6   (first position of 'S')
print(astring.count('l'))           # 2   (how many times 'l' appears)
print(astring.count('S '))          # 0   ('S' + space not found)
print(astring.startswith('Hel'))    # True
print(astring.endswith('rav'))      # True
print(astring.upper())              # HELLO SOURAV
print(astring.lower())              # hello sourav
print(astring.replace('Sourav', 'World'))   # Hello World
print("  hi  ".strip())             # "hi"  (removes surrounding spaces)

# ── Split: string → list ─────────────────────────
sentence = "Hello World! Bangladesh"
words = sentence.split()            # splits on whitespace by default
print(words)                        # ['Hello', 'World!', 'Bangladesh']

str1 = 'Md. Sourav Oyaj Abhi'
parts = str1.split()
print(parts)                        # ['Md.', 'Sourav', 'Oyaj', 'Abhi']
print(parts[0])                     # Md.

csv_line = "apple,banana,mango"
fruits = csv_line.split(',')        # split on comma
print(fruits)                       # ['apple', 'banana', 'mango']

# ── Multiline strings (triple quotes) ───────────
poem = '''my name is
 md sourav
 oyaj'''
print(poem)

# ── Concatenation ────────────────────────────────
e = "A"
print("A" + e)                      # AA
# print("Age: " + 23)              # ← TypeError! Must use str(23)
print("Age: " + str(23))           # Age: 23

# ── in / not in  (check if substring exists) ────
print("Sourav" in astring)         # True
print("Abhi" not in astring)       # True

# ── ASCII: chr() and ord() ───────────────────────
print(chr(65))                      # A  (number → character)
print(ord("A"))                     # 65 (character → number)
print(chr(97))                      # a  (lowercase a is 97)
print(chr(65) + "'s ASCII value is", ord("A"))

# ✅ TASK 1: From "Python Programming", print: length, first char, last char,
#            and the word "Program" using slicing.
# ✅ TASK 2: Reverse the string "Bangladesh" using slicing.
# ✅ TASK 3: Split "2024-12-31" by "-" and print year, month, day separately.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 5 — STRING FORMATTING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3 ways to embed variables inside strings.

fname = "Sourav"
score = 98
prize = 3000

# ── Method 1: + concatenation (old, messy) ────────
print("Hello, " + fname + "! You scored " + str(score))
# ↑ works but you need str() for numbers — annoying

# ── Method 2: .format()  (cleaner) ───────────────
# {} are placeholders filled in order
template = "Dear {}, Congrats! You won ${}, Enjoy."
print(template.format("Mohammad", 20))
print(template.format("Sourav",  3000))
print(template.format("Oyaj",    5000))

# Named placeholders (order doesn't matter)
msg = "Name: {name}, Age: {age}"
print(msg.format(name="Abhi", age=24))

# ── Method 3: f-strings (modern, recommended) ────
# Put f before the quote, use {} for any expression
print(f"Hello, {fname}! You scored {score}/100.")
print(f"Prize money: ${prize}")

# Math inside f-strings
x, y = 10, 3
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} - {y} = {x - y}")

# Format numbers with f-strings
pi = 3.14159265
print(f"Pi rounded: {pi:.2f}")          # 3.14  (2 decimal places)
print(f"Pi rounded: {pi:.4f}")          # 3.1416

# Multi-line example
a, b, c = "Mohammad", 20, "Dhaka"
c1, c2, c3 = "Sourav",  3000, "Chittagong"
names  = ["Mohammad", "Sourav", "Oyaj"]
prizes = [20,          3000,     5000]
for n, p in zip(names, prizes):
    print(f"Dear {n}, Congrats! You won ${p}, Enjoy.")

# ✅ TASK 1: Create a template "Hello {name}! You scored {score}/100."
#            Use .format() for 3 different students.
# ✅ TASK 2: Using f-strings, print a "receipt" with item name, qty, price,
#            and total (qty * price).


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 6 — BOOLEANS & COMPARISONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Booleans are True or False. Comparisons return booleans.

g, h = 3, 4

# Comparison operators
print(g < h)        # True   less than
print(g > h)        # False  greater than
print(g == h)       # False  equal to   (== not =)
print(g != h)       # True   not equal
print(g >= 3)       # True   greater than or equal
print(h <= 4)       # True   less than or equal
print(8 > 9)        # False

# Store a comparison result
is_greater = 3 < 4
print(is_greater)           # True
print(type(is_greater))     # <class 'bool'>

# Logical operators: and, or, not
print(True  and True)       # True   (both must be True)
print(True  and False)      # False
print(True  or  False)      # True   (at least one True)
print(False or  False)      # False
print(not True)             # False  (flips it)
print(not False)            # True

# Compound conditions
age, score = 17, 90
print(age > 18 and score > 80)     # False (age fails)
print(age > 18 or  score > 80)     # True  (score passes)

# hundred/tens example from original code
hundred = 100
tens    = 50
print(hundred > tens)              # True

# ✅ TASK 1: Check if a number is between 10 and 20 (inclusive) using 'and'.
# ✅ TASK 2: Check if a username is "admin" OR "superuser".


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 7 — OPERATORS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

a1, a2 = 9, 5

# ── Arithmetic operators ──────────────────────────
print('Sum     :', a1 + a2)         # 14
print('Sub     :', a1 - a2)         # 4
print('Mul     :', a1 * a2)         # 45
print('Div     :', a1 / a2)         # 1.8  ← always float
print('FloorDiv:', a1 // a2)        # 1    ← drops decimal
print('Mod     :', a1 % a2)         # 4    ← remainder (9 = 5×1 + 4)
print('Pow     :', a1 ** a2)        # 59049 ← 9 to the power of 5

# Useful: even/odd check with %
for n in range(1, 8):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

# ── Assignment operators ──────────────────────────
x = 10
x += 5;   print(x)      # 15  (x = x + 5)
x -= 3;   print(x)      # 12
x *= 2;   print(x)      # 24
x //= 5;  print(x)      # 4
x **= 2;  print(x)      # 16

# ── Big numbers — Python handles them! ────────────
# Unlike C/Java, Python integers have no size limit
big = 2 ** 100
print(big)              # 1267650600228229401496703205376

# ✅ TASK 1: a=15, b=4. Print sum, difference, product, quotient, remainder, a^b.
# ✅ TASK 2: Write a loop that prints only multiples of 3 from 1 to 30.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 8 — IF / ELIF / ELSE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Decision-making in Python. Indentation (4 spaces) is mandatory.

hundred, tens = 100, 50

if hundred > tens:
    print("hundred is greater than tens")
else:
    print("NO")

# ── if / elif / else chain ────────────────────────
color = 'blue'

if color == "Black":
    print("Color is black")
elif color == "Blue":           # ⚠️ case-sensitive! "Blue" ≠ "blue"
    print("Color is Blue")
elif color == "blue":
    print("Color is blue")      # ← this runs
else:
    print("Unknown color")

# ── Nested if ────────────────────────────────────
age      = 20
has_id   = True

if age >= 18:
    if has_id:
        print("You can enter the club")
    else:
        print("Bring your ID")
else:
    print("You are underage")

# ── Ternary / inline if ───────────────────────────
sc = 75
result = "Pass" if sc >= 50 else "Fail"
print(result)           # Pass

# ── Practical example: grade calculator ───────────
marks = 82

if marks >= 90:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
else:
    grade = 'F'
print(f"Marks: {marks} → Grade: {grade}")

# ✅ TASK 1: Write an if/elif/else that prints "Positive", "Negative", or "Zero".
# ✅ TASK 2: Check if a year is a leap year (divisible by 4, but not 100
#            unless also divisible by 400).


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 9 — MATCH / CASE  (Python 3.10+)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Like a switch statement in other languages.
# Clean alternative to long if/elif chains.

# Match with integer
a = 23
match a:
    case 23:
        print("this is number 23")
    case 12:
        print("Hello")
    case _:                 # _ is the default (like else)
        print("Last option")

# Match with string
day = "Monday"
match day:
    case "Monday":
        print("Start of the week!")
    case "Friday":
        print("Weekend is near!")
    case "Saturday" | "Sunday":     # | means OR
        print("Weekend!")
    case _:
        print("Regular weekday")

# Match with HTTP status codes
code = 404
match code:
    case 200:
        print("OK")
    case 301 | 302:
        print("Redirect")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status code")

# ✅ TASK: Create a match/case for seasons:
#   12, 1, 2 → "Winter";  3,4,5 → "Spring";  6,7,8 → "Summer";  9,10,11 → "Fall"


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 10 — WHILE LOOPS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Repeats a block as long as the condition stays True.
# ⚠️ Always update the variable or you get an infinite loop!

# Basic while
i = 1
while i < 5:
    print(i)            # prints 1, 2, 3, 4
    i = i + 1           # MUST update i each iteration

# While with break (exit the loop early)
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        print("i=3, stopping!")
        break               # jumps out of the loop immediately

# While with continue (skip current iteration)
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue            # skips printing 3
    print(i)                # prints 1, 2, 4, 5

# Practical: countdown timer
n = 5
while n > 0:
    print(f"Countdown: {n}")
    n -= 1
print("Go!")

# Practical: sum of digits
num = 12345
total = 0
temp = num
while temp > 0:
    total += temp % 10      # grab last digit
    temp  //= 10            # remove last digit
print(f"Sum of digits of {num} =", total)    # 15

# ⚠️ BROKEN loop from original code (DO NOT RUN):
# i = 1
# while i < 6:
#     print(i)          ← i never changes → infinite loop!
# print("Abhi")         ← this line is NEVER reached

# ✅ TASK 1: Use while to print the 3× multiplication table (3×1 to 3×10).
# ✅ TASK 2: Use while to find the first power of 2 that exceeds 1000.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 11 — FOR LOOPS & RANGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# for loops iterate over any sequence: list, string, range, etc.

objects = ["obj", "obj1", "obj3"]
for x in objects:
    print(x)
print(objects)              # the list itself is unchanged

# ── range(start, stop, step) ──────────────────────
# stop is NOT included; start defaults to 0; step defaults to 1

for i in range(1, 6):       # 1 to 5
    print(i)

# Multiplication table of 5
for i in range(0, 11):
    print(5, "×", i, "=", 5 * i)

# Even numbers
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# Countdown
for i in range(10, 0, -1):
    print(i, end=" ")
print("Blast off! 🚀")

# ── Loop over a string ────────────────────────────
word = "abhi"
print(word[0])                  # a (index access)
for i in range(len(word)):
    print(word[i], end=" ")     # a b h i
print()

for letter in word:             # cleaner way
    print(letter, end=" ")
print()

# ── enumerate: gives index AND value ─────────────
for idx, ch in enumerate("hello"):
    print(f"[{idx}] → {ch}")

# ── zip: loop two lists together ──────────────────
names  = ["Sourav", "Abhi", "Tanvir"]
grades = [90,        85,     78]
for n, g in zip(names, grades):
    print(f"{n}: {g}")

# ── Nested for loops ──────────────────────────────
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()

# ── break / continue inside for ───────────────────
for n in range(1, 10):
    if n == 5:
        break               # stop at 5
    print(n, end=" ")
print()

for n in range(1, 10):
    if n % 2 == 0:
        continue            # skip even numbers
    print(n, end=" ")       # 1 3 5 7 9
print()

# ✅ TASK 1: Print all numbers from 1-100 that are divisible by 7.
# ✅ TASK 2: Print the 7× table from 7×1 to 7×12 using range.
# ✅ TASK 3: Print a right-angled triangle of stars using nested loops:
#            Row 1: *
#            Row 2: **
#            Row 3: ***  etc.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 12 — FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Functions are reusable named blocks of code.
# Define once, call many times.

# ── Basic function ────────────────────────────────
def greet(name):
    print(name)
    print("I am learning Python")
    print("My name is", name)

greet("Md Sourav Oyaj")
greet("Abhi")

# ── Function with return value ────────────────────
def add(a, b):
    result = a + b
    return result               # sends value back to caller

total = add(10, 20)
print(total)                    # 30
print(add(100, 200))            # 300  (use directly in print)

# ── Multiple parameters ────────────────────────────
def calc_sum(val1, val2):
    result = val1 + val2
    print(result)

calc_sum(12, 13)                # 25

# ── Return vs print ────────────────────────────────
# print()  → shows on screen, gives None back
# return   → gives value back to caller, use it later

def get_double(n):
    return n * 2

d = get_double(5)
print(d)                        # 10
print(get_double(7) + 1)        # 15

# ── Average of 3 numbers ──────────────────────────
def average(a, b, c):
    d = (a + b + c) / 3
    print("Inside function:", d)
    return d

avg1 = average(2, 6, 3)
print("Outside:", avg1)         # 3.666...

# ── Default parameters ─────────────────────────────
# If caller doesn't pass, Python uses the default
def add_plus(a, b, c, plus=10):
    return a + b + c + plus

print(add_plus(10, 20, 30))         # 70   (uses plus=10)
print(add_plus(10, 20, 30, 40))     # 100  (overrides to 40)

# ── Keyword arguments ─────────────────────────────
# Pass by name → order doesn't matter
def show_student(name, age):
    print(f"Name: {name}  Age: {age}")

show_student(name="Sourav", age=23)
show_student(age=24, name="Abhi")   # different order, same result

# ── Docstring ─────────────────────────────────────
# Triple-quoted string right after def line = documentation
def doc_sum(a, b):
    """This is a sum function for 2 numbers.
    Returns the sum of a and b."""
    return a + b

print(doc_sum.__doc__)              # shows the documentation
print(doc_sum(3, 7))                # 10

# ── *args: variable number of arguments ──────────
def multi_add(*nums):
    return sum(nums)

print(multi_add(1, 2, 3))          # 6
print(multi_add(1, 2, 3, 4, 5))    # 15

# ✅ TASK 1: Write a function that takes name and age and returns a greeting.
# ✅ TASK 2: Write a function that takes 3 numbers and returns the largest.
# ✅ TASK 3: Write a function celsius_to_fahrenheit(c) with correct formula.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 13 — LAMBDA (Anonymous Functions)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# One-line function without a name.
# Syntax:  lambda parameters : expression

sq  = lambda x     : x * x
print(sq(2))        # 4
print(sq(5))        # 25

add = lambda x, y  : x + y
print(add(2, 3))    # 5

greet = lambda name: f"Hello, {name}!"
print(greet("Sourav"))

# Ternary inside lambda
check = lambda age: "Adult" if age >= 18 else "Minor"
print(check(20))    # Adult
print(check(15))    # Minor

# ── map(): apply a function to every item in a list ──
nums    = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)      # [1, 4, 9, 16, 25]

# ── filter(): keep only items where function returns True ──
evens   = list(filter(lambda x: x % 2 == 0, nums))
print(evens)        # [2, 4]

# ── sorted() with key ─────────────────────────────
words = ["banana", "apple", "cherry", "date"]
print(sorted(words))                        # alphabetical
print(sorted(words, key=lambda w: len(w)))  # by length

# ✅ TASK 1: Write a lambda that takes a number and returns "Even" or "Odd".
# ✅ TASK 2: Use map() to convert a list of Celsius temps to Fahrenheit.
# ✅ TASK 3: Use filter() to keep only words longer than 4 letters.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 14 — RECURSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A function that calls itself.
# ⚠️ MUST have a base case — otherwise it recurses forever!

# ── Fibonacci sequence: 0 1 1 2 3 5 8 13 21 ...
# Formula: fib(n) = fib(n-2) + fib(n-1)
# Base:    fib(0) = 0,  fib(1) = 1

def fib(n):
    if n == 0 or n == 1:            # BASE CASE — stops recursion
        return n
    return fib(n - 1) + fib(n - 2)  # recursive call

# Print fibonacci from index 0 to 8
s, e = 0, 8
for i in range(s, e + 1):
    print(fib(i), end=" ")          # 0 1 1 2 3 5 8 13 21
print()

# ── Factorial: n! = n × (n-1) × ... × 1
# fac(5) = 5 × fac(4) = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    if n == 0 or n == 1:            # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 120
print(factorial(0))     # 1
print(factorial(10))    # 3628800

# ── Countdown with recursion ──────────────────────
def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

countdown(5)

# ✅ TASK 1: Write a recursive function that sums all numbers from 1 to n.
# ✅ TASK 2: Write a recursive function that reverses a string.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 15 — USER INPUT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# input() pauses the program and waits for the user to type.
# ⚠️ input() ALWAYS returns a STRING — cast to int/float when needed!

# ── Basic input ───────────────────────────────────
# username = input()
# print(username)

# ── Input with prompt text ─────────────────────────
# name = input("Enter your name: ")
# print("Your Name is:", name)
# print("Your Name is: " + name)

# ── Integer input ─────────────────────────────────
# age = int(input("Age: "))
# if age > 18:
#     print("Can drive")
# elif age == 18:
#     print("Just turned 18, can drive!")
# else:
#     print("Too young to drive")

# ── Two numbers on one line ────────────────────────
# a, b = map(int, input("Enter two numbers: ").split())
# print(f"{a} + {b} = {a + b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} - {b} = {a - b}")

# ── Multiple words from input ─────────────────────
# a = input().split()       # input: "Hello World Python"
# print(a[0])               # Hello
# print(a[1])               # World
# print(a[2])               # Python

# ── Demonstrate WITHOUT actual input (simulated) ──
line = "50 30"                      # pretend user typed this
a, b = map(int, line.split())
print(f"{a} + {b} = {a + b}")       # 50 + 30 = 80
print(f"{a} * {b} = {a * b}")       # 50 * 30 = 1500
print(f"{a} - {b} = {a - b}")       # 50 - 30 = 20

parts = "Hello World Python".split()
print(parts[0], parts[1], parts[2])  # Hello World Python

# ✅ TASK: Write a program that asks for length and width (as ints on one
#          line) and prints the area and perimeter of a rectangle.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 16 — TRY / EXCEPT (Error Handling)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Prevents your program from crashing when errors happen.

# ── Basic: catch any error ─────────────────────────
try:
    print(p)                        # p is not defined → NameError
except:
    print("p not found")            # this runs, no crash

# ── Catch specific error types ─────────────────────
try:
    x = int("hello")                # ValueError
except ValueError:
    print("That's not a number!")

try:
    nums = [1, 2, 3]
    print(nums[10])                 # IndexError
except IndexError:
    print("Index out of range!")

try:
    result = 10 / 0                 # ZeroDivisionError
except ZeroDivisionError:
    print("Can't divide by zero!")

# ── Multiple except blocks ─────────────────────────
try:
    val = int("abc")
except ValueError:
    print("Bad value — not a number")
except TypeError:
    print("Wrong type used")
except Exception as e:
    print(f"Some other error: {e}")

# ── else and finally ──────────────────────────────
# else   : runs only if NO exception happened
# finally: runs ALWAYS (great for cleanup)
try:
    val = int("123")
except ValueError:
    print("Bad input")
else:
    print("Conversion worked:", val)    # runs (no error happened)
finally:
    print("Done (this always runs)")

# ── Practical: safe division function ─────────────
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error: division by zero

# ✅ TASK 1: Write a function that safely converts a string to int,
#            returning 0 if conversion fails.
# ✅ TASK 2: Write a safe_index(lst, i) that returns None if index is invalid.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 17 — MATH MODULE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import math

print(math.sqrt(16))            # 4.0   square root
print(int(math.sqrt(16)))       # 4     convert to int

print(math.pi)                  # 3.141592653589793
print(math.floor(3.9))          # 3     round DOWN always
print(math.ceil(3.1))           # 4     round UP always
print(math.pow(2, 10))          # 1024.0  (2^10)
print(math.factorial(5))        # 120
print(math.log(100, 10))        # 2.0   log base 10 of 100
print(math.log2(8))             # 3.0   log base 2 of 8

# abs() is built-in, NOT math.abs (common mistake!)
print(abs(-42))                 # 42

# Hypotenuse of right triangle with sides 3 and 4
hyp = math.sqrt(3**2 + 4**2)
print(hyp)                      # 5.0
# Or use math.hypot directly:
print(math.hypot(3, 4))         # 5.0

# ✅ TASK 1: Calculate the area of a circle with radius 7 (area = π × r²).
# ✅ TASK 2: Find the hypotenuse of a triangle with sides 5 and 12.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 18 — JSON MODULE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# JSON = JavaScript Object Notation — universal data exchange format.
# In Python, it looks like a dict but uses DOUBLE QUOTES everywhere.
import json

# ── JSON string → Python dict  (json.loads) ───────
x = '{"name": "abhi", "age": 24, "city": "akbarshah"}'
y = json.loads(x)
print(y)                # {'name': 'abhi', 'age': 24, 'city': 'akbarshah'}
print(y["name"])        # abhi
print(type(y))          # <class 'dict'>

# ── Python dict → JSON string  (json.dumps) ───────
# DEFINE xx FIRST before using it!
xx = {"name": "abhi", "age": 24, "city": "akbarshah"}
dict_to_json = json.dumps(xx)
print(dict_to_json)         # {"name": "abhi", "age": 24, "city": "akbarshah"}
print(type(dict_to_json))   # <class 'str'>
# ⚠️ BUG FIX: in the original code print(xx) appeared BEFORE xx was defined
#              → NameError. Always define before using!

# Pretty-print with indentation
pretty = json.dumps(xx, indent=4)
print(pretty)

# ── Key rule ──────────────────────────────────────
# Python dict  → single OR double quotes internally
# JSON         → ALWAYS double quotes
# json.dumps() converts dict to JSON (double-quote) string
# json.loads() converts JSON string back to dict

# ✅ TASK 1: Create a dict with your own info, convert to JSON, print it.
# ✅ TASK 2: Take a JSON string of a student and extract just the name.


# ============================================================
#  END OF FILE 1 — PYTHON BASICS
#  Next: 02_python_collections.py  →  List, Tuple, Set, Dict
# ============================================================
