# ============================================================
#   ⚡  ADVANCED PYTHON — Functions & Error Handling
# ============================================================
#   Author  : Md Sourav Oyaj
#   Topics  : raise (manual exceptions)
#             try / except / finally  (advanced patterns)
#             while True + try/except (safe input loop)
#             map()  with named functions
#             filter() with named functions
#             reduce() from functools
#             Walrus Operator :=  (assignment expression)
#             *args   (variable positional arguments)
#             **kwargs (variable keyword arguments)
#             *args + **kwargs  combined
#   Prerequisite: 01_python_basics.py
# ============================================================


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 1 — raise  (Manually Throwing Exceptions)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# You've seen try/except catch errors that Python raises.
# With 'raise' YOU can trigger an error intentionally
# when input breaks your rules — protecting bad data from
# entering your program.

# ── Basic raise ───────────────────────────────────
# (simulating user input with hardcoded values for demo)

a = 10
b = 0                           # pretend user typed 0

if b == 0:
    raise ValueError("Please don't divide by zero")
# ↑ This stops the program here with a clear message.
# Without raise, a/b would give ZeroDivisionError (Python's generic msg).
# With raise, you write YOUR OWN error message.

# ── raise inside a function ───────────────────────
# NOTE: comment out the block above before running this section

def safe_divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a / b

# Wrap the call in try/except to handle your own raised errors:
try:
    print(safe_divide(10, 2))       # 5.0
    print(safe_divide(10, 0))       # raises ValueError
except ValueError as e:
    print(f"ValueError caught: {e}")

try:
    print(safe_divide(10, "two"))   # raises TypeError
except TypeError as e:
    print(f"TypeError caught: {e}")

# ── Common exception types to raise ───────────────
# ValueError   → value is wrong type or out of range
# TypeError    → wrong argument type
# IndexError   → index out of bounds
# KeyError     → key not found in dict
# FileNotFoundError → file doesn't exist
# PermissionError   → no access rights

# ── Validating input with raise ───────────────────
def create_student(name, age, gpa):
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    if not (0 <= age <= 150):
        raise ValueError(f"Age {age} is out of valid range (0-150)")
    if not (0.0 <= gpa <= 4.0):
        raise ValueError(f"GPA {gpa} must be between 0.0 and 4.0")
    return {"name": name, "age": age, "gpa": gpa}

try:
    s = create_student("Sourav", 23, 3.5)
    print(s)                            # works fine
except ValueError as e:
    print(e)

try:
    s = create_student("", 23, 3.5)    # empty name
except ValueError as e:
    print(e)                            # Name must be a non-empty string

try:
    s = create_student("Abhi", 23, 5.0)  # GPA too high
except ValueError as e:
    print(e)                            # GPA 5.0 must be between 0.0 and 4.0

# ── Chaining exceptions (re-raise) ────────────────
def load_data(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Could not load '{filename}'") from e

try:
    load_data("missing_file.txt")
except RuntimeError as e:
    print(e)                        # Could not load 'missing_file.txt'

# ✅ TASK 1: Write a function set_age(age) that raises ValueError
#   if age < 0 or age > 150.
# ✅ TASK 2: Write a function get_item(lst, index) that raises a
#   custom IndexError message instead of Python's default.
# ✅ TASK 3: What is the difference between raise and return?
#   Write your answer as a comment.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 2 — try / except / finally  (Advanced)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# You already know basic try/except (see 01_python_basics.py).
# Here: 'except Exception as e', 'finally', and real patterns.

# ── except Exception as e ─────────────────────────
# 'Exception' is the BASE class of most exceptions.
# 'as e' stores the error object — so you can PRINT what went wrong.

def divide(a, b):
    try:
        c = a / b
        return c
    except Exception as e:          # catches ANY standard exception
        print(e)                    # prints the actual error message
        return None
    finally:
        print("This is always executed")  # runs no matter what!

# ── finally always runs ────────────────────────────
# (simulating input — remove # to use real input)
a = 10
b = 2
result = divide(a, b)
# prints: "This is always executed"
# returns: 5.0
if result is not None:
    print(f"Result: {result}")

a = 10
b = 0
result = divide(a, b)
# prints: "division by zero"
# prints: "This is always executed"
# returns: None

# ── Why is finally useful? ─────────────────────────
# Resources (files, database connections, network sockets)
# MUST be closed even when an error happens.
# finally ensures cleanup always runs.

def read_file(path):
    f = None
    try:
        f = open(path, 'r')
        return f.read()
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return ""
    finally:
        if f:
            f.close()               # file is ALWAYS closed, even on error
        print("Cleanup done.")

data = read_file("does_not_exist.txt")
# File 'does_not_exist.txt' not found
# Cleanup done.

# ── try / except / else / finally  (full form) ────
# else  → runs ONLY if NO exception occurred
# finally → runs ALWAYS

def parse_int(s):
    try:
        val = int(s)
    except ValueError:
        print(f"'{s}' is not a valid integer")
        return None
    else:
        print(f"Parsing succeeded: {val}")  # only if no error
        return val
    finally:
        print("parse_int() finished")       # always

print(parse_int("42"))      # succeeds
print(parse_int("hello"))   # fails

# ── Multiple except blocks ─────────────────────────
def risky(lst, idx, div):
    try:
        val = lst[idx]          # may raise IndexError
        res = val / div         # may raise ZeroDivisionError or TypeError
        return res
    except IndexError:
        print(f"No item at index {idx}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError as e:
        print(f"Type error: {e}")
    except Exception as e:
        print(f"Unexpected: {e}")   # catch-all safety net (put last)
    finally:
        print("risky() completed")

risky([10, 20, 30], 1, 4)       # 5.0
risky([10, 20, 30], 9, 4)       # IndexError
risky([10, 20, 30], 1, 0)       # ZeroDivisionError

# ✅ TASK 1: Write a function safe_open(filename) that:
#   - Returns file contents if it exists
#   - Prints "File not found" if missing
#   - ALWAYS prints "Operation done" in finally
# ✅ TASK 2: What does 'except Exception as e' catch that
#   'except ValueError' does NOT? Write examples.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 3 — while True + try/except  (Safe Input Loop)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A common real-world pattern: keep asking for input until
# the user enters something valid. Combines loops + exceptions.

# ── Commented pattern (remove # to run interactively) ─────

# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"Sum: {a + b}")
#         break                           # success → exit loop
#     except Exception as e:
#         print("Error occurred:", e)     # bad input → loop again

# ── How it works ──────────────────────────────────
# Step 1: while True creates an infinite loop
# Step 2: try asks for input and converts to int
# Step 3: if user types "abc" → ValueError → except runs → loop again
# Step 4: if input is valid → sum prints → break exits the loop

# ── Simulated demo without actual input ───────────
inputs = ["abc", "hello", "10", "5"]   # pretend these were typed
idx    = 0
a = b  = None

while True:
    try:
        a = int(inputs[idx]);  idx += 1
        b = int(inputs[idx]);  idx += 1
        print(f"Sum: {a + b}")
        break
    except (ValueError, IndexError) as e:
        print(f"Error: {e} — try again")

# ── Adding a quit option ───────────────────────────
# while True:
#     raw = input("Enter a number (or 'q' to quit): ")
#     if raw.lower() == 'q':
#         print("Bye!")
#         break
#     try:
#         n = int(raw)
#         print(f"You entered: {n}")
#     except ValueError:
#         print("That's not a number, try again.")

# ── Collect items until 'q' ────────────────────────
# (from original code — uses walrus operator, explained in Section 5)
# list1 = []
# while (data := input()):
#     list1.append(data)
#     print(data)
#     if data == "q":
#         break
# print(list1)

# ✅ TASK: Write a loop that keeps asking for a positive number.
#   If the user types a negative number, say "Must be positive, try again."
#   If they type non-numeric text, say "Not a number, try again."
#   When a valid positive number is entered, print its square and stop.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 4 — map()  (Apply function to every item)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# map(function, iterable) → applies the function to EVERY item.
# Returns a map object — wrap in list() to see the results.
# You can use a named function OR a lambda.

numbers = [1, 2, 3, 4, 5, 6, 9, 90, 65]

# ── With a named function ──────────────────────────
def sq(x):
    return x * x

new = list(map(sq, numbers))
print(new)                  # [1, 4, 9, 16, 25, 36, 81, 8100, 4225]

# ── With a lambda (shorter) ───────────────────────
new2 = list(map(lambda x: x * x, numbers))
print(new2)                 # same result

# ── More map() examples ───────────────────────────
words = ["hello", "world", "python"]

# uppercase all words
upper = list(map(str.upper, words))     # str.upper is a method reference
print(upper)                            # ['HELLO', 'WORLD', 'PYTHON']

# get length of each word
lengths = list(map(len, words))
print(lengths)                          # [5, 5, 6]

# convert strings to ints
str_nums = ["1", "2", "3", "4"]
ints = list(map(int, str_nums))
print(ints)                             # [1, 2, 3, 4]

# celsius to fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)                       # [32.0, 68.0, 98.6, 212.0]

# ── map() with two iterables ──────────────────────
a = [1, 2, 3]
b = [10, 20, 30]
added = list(map(lambda x, y: x + y, a, b))
print(added)                            # [11, 22, 33]

# ── map vs for loop — same result, different style ─
result_loop = []
for x in numbers:
    result_loop.append(x * x)
result_map = list(map(lambda x: x * x, numbers))
print(result_loop == result_map)        # True — identical output

# ✅ TASK 1: Use map() to convert a list of names to title case.
# ✅ TASK 2: Use map() to double every number in [5, 10, 15, 20].
# ✅ TASK 3: Use map() with TWO lists to compute the product of each pair:
#   [1,2,3] × [4,5,6] → [4, 10, 18]


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 5 — filter()  (Keep only matching items)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# filter(function, iterable) → keeps only items where function returns True.
# map()   → transforms every item    (returns same count)
# filter()→ selects certain items    (returns fewer or equal count)

numbers = [1, 2, 3, 4, 5, 6, 9, 90, 65]

# ── With a named function ──────────────────────────
def is_greater_9(x):
    if x > 9:
        return True
    else:
        return False

n = list(filter(is_greater_9, numbers))
print(n)                    # [90, 65]  ← only values > 9 are kept

# Original code comment: "if I use map it returns booleans but
# filter returns the actual VALUE" — great observation! Let's prove it:
map_result    = list(map(is_greater_9, numbers))
filter_result = list(filter(is_greater_9, numbers))
print("map()   result:", map_result)        # [False, False, ..., True, True]  ← booleans
print("filter() result:", filter_result)    # [90, 65]  ← actual values

# ── With a lambda (shorter) ───────────────────────
n2 = list(filter(lambda x: x > 9, numbers))
print(n2)                   # [90, 65]

# ── More filter() examples ────────────────────────
words = ["apple", "banana", "fig", "mango", "kiwi", "blueberry"]

# only words longer than 4 characters
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)           # ['apple', 'banana', 'mango', 'blueberry']

# only even numbers
evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(evens)                # [2, 4, 6, 8, 10]

# only non-empty strings
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, strings))     # None as function = filter falsy values
print(non_empty)            # ['hello', 'world', 'python']

# only positive numbers
mixed = [-3, 0, 5, -1, 8, -7, 2]
positives = list(filter(lambda x: x > 0, mixed))
print(positives)            # [5, 8, 2]

# ── Chaining map() and filter() ───────────────────
# Square only the numbers greater than 3
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda x: x > 3, nums)))
print(result)               # [16, 25, 36]

# Step by step (more readable):
filtered = filter(lambda x: x > 3, nums)   # [4, 5, 6]
squared  = map(lambda x: x**2, filtered)   # [16, 25, 36]
print(list(squared))

# ✅ TASK 1: From [3, 7, 1, 15, 22, 8, 11], filter numbers divisible by 3.
# ✅ TASK 2: From a list of names, filter only those starting with 'A'.
# ✅ TASK 3: Chain filter + map: from [1..20], keep even numbers then cube them.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 6 — reduce()  (Combine all items into one)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# reduce(function, iterable) → applies function cumulatively
# to reduce the entire list to a SINGLE value.
# Must import from functools.
#
# Example: reduce(add, [1,2,3,4,5])
#   Step 1: add(1, 2) = 3
#   Step 2: add(3, 3) = 6
#   Step 3: add(6, 4) = 10
#   Step 4: add(10,5) = 15

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# ── With a named function ──────────────────────────
def add(a, b):
    return a + b

total = reduce(add, numbers)
print(total)                # 15

# ── With a lambda ─────────────────────────────────
total2 = reduce(lambda a, b: a + b, numbers)
print(total2)               # 15

# ── More reduce() examples ────────────────────────

# Product of all numbers
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(product)              # 120  (1×2×3×4×5)

# Find maximum value (without using max())
nums = [3, 1, 9, 2, 7, 5]
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)              # 9

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda a, b: a + b, words)
print(sentence)             # Hello World!

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print(flat)                 # [1, 2, 3, 4, 5, 6]

# ── reduce() with initial value ────────────────────
# 3rd argument = starting value (useful for empty lists)
total3 = reduce(lambda a, b: a + b, [1, 2, 3], 100)
print(total3)               # 106  (starts accumulating from 100)

# ── map vs filter vs reduce — summary ─────────────
# +──────────────+────────────────────────+──────────────────────+
# │              │  Input → Output        │  What it does        │
# +──────────────+────────────────────────+──────────────────────+
# │  map()       │  [a,b,c] → [f(a),f(b),f(c)]  │ Transform each item  │
# │  filter()    │  [a,b,c] → [a,c] (subset)     │ Keep matching items  │
# │  reduce()    │  [a,b,c] → single value        │ Combine into one     │
# +──────────────+────────────────────────+──────────────────────+

nums = [1, 2, 3, 4, 5]
print("map:   ", list(map(lambda x: x*2, nums)))         # [2,4,6,8,10]
print("filter:", list(filter(lambda x: x>2, nums)))      # [3,4,5]
print("reduce:", reduce(lambda a,b: a+b, nums))          # 15

# ✅ TASK 1: Use reduce() to find the MINIMUM in a list (without min()).
# ✅ TASK 2: Use reduce() to compute 10! (10 factorial = 10×9×8×...×1).
# ✅ TASK 3: Use map, filter, and reduce together:
#   From [1..10]: keep odds → square them → sum them all.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 7 — WALRUS OPERATOR  :=  (Python 3.8+)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# := is the "assignment expression" or "walrus operator".
# It ASSIGNS a value AND USES it in the SAME expression.
# Avoids calling a slow/repeated function twice.

# ── Problem it solves ─────────────────────────────
def very_slow_fun():
    print("Something.....")
    print("Something.....")
    print("Something.....")
    return 70

# OLD way: call function, store, then check
a = very_slow_fun()
if a > 10:
    print(a)
else:
    print("Not greater than 10")
# ↑ Function called once, stored in 'a', then 'a' is checked.

# NEW way (walrus): assign AND check in ONE expression
if (a := very_slow_fun()) > 10:    # a gets assigned 70, then 70 > 10
    print(a)
else:
    print("Not greater than 10")
# ↑ Same result, but reads as one step.
# Note the outer parentheses — needed for operator precedence!

# ── Walrus in a while loop ────────────────────────
# From original code: collect items until 'q' is typed
# list1 = []
# while (data := input()):           # data = input(), then check truthiness
#     list1.append(data)
#     print(data)
#     if data == "q":
#         break
# print(list1)

# Simulated version (no actual input):
simulated_inputs = iter(["apple", "banana", "q"])
list1 = []
while (data := next(simulated_inputs, "")):  # gets next item, stops on ""
    list1.append(data)
    print(data)
    if data == "q":
        break
print(list1)                # ['apple', 'banana', 'q']

# ── More walrus examples ───────────────────────────

# Without walrus: compute len twice
text = "Hello Bangladesh"
if len(text) > 10:
    print(f"Long string: {len(text)} chars")

# With walrus: compute once, reuse
if (n := len(text)) > 10:
    print(f"Long string: {n} chars")

# In a list comprehension (find and keep only valid results)
def parse_num(s):
    try:
        return int(s)
    except ValueError:
        return None

raw = ["1", "abc", "3", "bad", "5"]
parsed = [n for s in raw if (n := parse_num(s)) is not None]
print(parsed)               # [1, 3, 5]

# Processing a stream until done
data_stream = iter([5, 12, 3, 99, 7, -1])   # -1 signals end
results = []
while (val := next(data_stream, None)) is not None and val != -1:
    results.append(val * 2)
print(results)              # [10, 24, 6, 198, 14]

# ✅ TASK 1: Use walrus in a while loop that reads numbers and accumulates
#   them until the total exceeds 100. Print each number as it's added.
# ✅ TASK 2: Use walrus in a list comprehension to keep only
#   results of a function that aren't None.
# ✅ TASK 3: Rewrite this without walrus:
#   if (match := re.search(r'\d+', text)): print(match.group())


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 8 — *args  (Variable Positional Arguments)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# *args lets a function accept ANY NUMBER of positional arguments.
# Inside the function, 'args' is a TUPLE of all passed values.
# The name 'args' is a convention — you could write *nums, *values etc.

def total(*args):           # args will be a tuple
    tot = 0
    for item in args:
        tot += item
    return tot

print(total(4, 3, 2, 10))  # 19
print(total(1, 2))         # 3
print(total(100))           # 100
print(total())              # 0  (empty tuple)

# ── What does args look like inside? ─────────────
def show_args(*args):
    print(f"args is: {args}")
    print(f"type  : {type(args)}")
    for i, val in enumerate(args):
        print(f"  [{i}] = {val}")

show_args(10, 20, 30)
# args is: (10, 20, 30)
# type  : <class 'tuple'>

# ── *args + regular params ─────────────────────────
# Regular params must come BEFORE *args
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Sourav", "Abhi", "Tanvir")
# Hello, Sourav!
# Hello, Abhi!
# Hello, Tanvir!

# ── Practical: statistics function ────────────────
def stats(*nums):
    if not nums:
        return None
    return {
        "count": len(nums),
        "sum"  : sum(nums),
        "avg"  : sum(nums) / len(nums),
        "min"  : min(nums),
        "max"  : max(nums),
    }

print(stats(10, 20, 30, 40, 50))
# {'count': 5, 'sum': 150, 'avg': 30.0, 'min': 10, 'max': 50}

# ── Unpacking a list into *args ────────────────────
def add3(a, b, c):
    return a + b + c

values = [1, 2, 3]
print(add3(*values))    # 6  ← * unpacks the list into separate args

# ✅ TASK 1: Write a function multiply(*args) that multiplies all numbers together.
# ✅ TASK 2: Write a function sentence(sep, *words) that joins words with sep.
#   Example: sentence("-", "Hello", "World") → "Hello-World"
# ✅ TASK 3: What type is 'args' inside the function? Test it.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 9 — **kwargs (Variable Keyword Arguments)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# **kwargs lets a function accept ANY NUMBER of keyword arguments.
# Inside the function, 'kwargs' is a DICT of {name: value} pairs.
# The name 'kwargs' is a convention — any name after ** works.

def show_marks(**kwargs):       # kwargs is a dictionary
    for key in kwargs.keys():
        print(f"{key} = {kwargs[key]}")

show_marks(Abhi=3.2, Sifaet=3.2, Reaz=3.1)
# Abhi = 3.2
# Sifaet = 3.2
# Reaz = 3.1

# ── What does kwargs look like inside? ───────────
def inspect_kwargs(**kwargs):
    print(f"kwargs : {kwargs}")
    print(f"type   : {type(kwargs)}")
    for key, val in kwargs.items():
        print(f"  {key!r} → {val!r}")

inspect_kwargs(name="Sourav", age=23, city="Dhaka")
# kwargs : {'name': 'Sourav', 'age': 23, 'city': 'Dhaka'}
# type   : <class 'dict'>

# ── **kwargs + regular params ──────────────────────
# Regular params must come BEFORE **kwargs
def register(username, **info):
    print(f"Username : {username}")
    for k, v in info.items():
        print(f"  {k}: {v}")

register("sourav_99", email="s@test.com", age=23, city="Dhaka")

# ── Practical: config builder ──────────────────────
def build_config(**settings):
    defaults = {"debug": False, "port": 8080, "host": "localhost"}
    defaults.update(settings)       # override defaults with passed values
    return defaults

cfg = build_config(debug=True, port=3000)
print(cfg)
# {'debug': True, 'port': 3000, 'host': 'localhost'}

# ── Unpacking a dict into **kwargs ────────────────
def display(name, age, city):
    print(f"{name} | {age} | {city}")

data = {"name": "Abhi", "age": 24, "city": "Dhaka"}
display(**data)             # ** unpacks dict into keyword args

# ✅ TASK 1: Write a function create_profile(**kwargs) that prints each
#   key-value pair with the key capitalized.
# ✅ TASK 2: Write a function merge(**dict1, **dict2) — wait, that won't work.
#   How WOULD you merge two dicts passed as kwargs? Try it.
# ✅ TASK 3: What type is 'kwargs' inside the function? Test it.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 10 — *args  +  **kwargs  (Combined)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# You can use both together — the most flexible function signature.
# ORDER RULE:  regular params → *args → **kwargs
#              (you CANNOT change this order)

def func1(*args, **kwargs):
    print("args  :", args)      # tuple of positional args
    print("kwargs:", kwargs)    # dict of keyword args

func1(1, 2, 3, 4, Abhi=3.2, Sifaet=3.2, Reaz=3.1)
# args  : (1, 2, 3, 4)
# kwargs: {'Abhi': 3.2, 'Sifaet': 3.2, 'Reaz': 3.1}

# ── All three together ─────────────────────────────
def full_func(required, *args, **kwargs):
    print(f"required : {required}")
    print(f"args     : {args}")
    print(f"kwargs   : {kwargs}")

full_func("must", 1, 2, 3, name="Sourav", age=23)
# required : must
# args     : (1, 2, 3)
# kwargs   : {'name': 'Sourav', 'age': 23}

# ── Real-world example: logging function ──────────
def log(level, *messages, **context):
    prefix = f"[{level.upper()}]"
    msg    = " ".join(str(m) for m in messages)
    ctx    = " | ".join(f"{k}={v}" for k, v in context.items())
    print(f"{prefix} {msg}  {ctx}" if ctx else f"{prefix} {msg}")

log("info",  "Server started")
log("warn",  "Memory high", "Swap used", host="prod-01", cpu=88)
log("error", "DB connection failed", db="postgres", retry=3)

# ── Forwarding args/kwargs to another function ────
# Very common in decorators and wrappers!
def wrapper(*args, **kwargs):
    print("Before call")
    result = func1(*args, **kwargs)   # pass everything through
    print("After call")
    return result

wrapper(10, 20, x="hello")

# ── Order matters — this would be a SyntaxError ───
# def wrong(**kwargs, *args):  ← SyntaxError! kwargs must come last
# def wrong(*args, regular):   ← if regular comes after *args, it must
#                                  be passed as a keyword argument only

# ── Summary ───────────────────────────────────────
# +───────────────+──────────────+────────────────────────+
# │               │  Syntax      │  Inside function        │
# +───────────────+──────────────+────────────────────────+
# │ Regular param │  param       │  single value          │
# │ *args         │  *name       │  tuple of values       │
# │ **kwargs      │  **name      │  dict {key: value}     │
# +───────────────+──────────────+────────────────────────+
# Order: regular → *args → keyword-only → **kwargs

# ✅ TASK 1: Write a function describe(name, *hobbies, **details) that:
#   - Prints "Name: {name}"
#   - Prints each hobby from *hobbies
#   - Prints each key-value from **details
#   Call it: describe("Sourav", "coding", "gaming", age=23, city="Dhaka")

# ✅ TASK 2: Write a decorator using *args, **kwargs that prints
#   "Function called" before and "Function done" after any function.

# ✅ TASK 3: What happens if you pass a keyword argument BEFORE
#   positional arguments? e.g. func(name="hi", 1, 2) — try it and explain.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  BONUS — ALL FUNCTIONAL TOOLS SIDE BY SIDE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() — double every number
doubled = list(map(lambda x: x * 2, nums))
print("map()   :", doubled)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter() — keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("filter():", evens)
# [2, 4, 6, 8, 10]

# reduce() — sum all numbers
total = reduce(lambda a, b: a + b, nums)
print("reduce():", total)
# 55

# Combined pipeline:
# From 1..10: keep evens → square them → sum them
result = reduce(
    lambda a, b: a + b,
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, nums))
)
print("pipeline:", result)      # 4+16+36+64+100 = 220

# Equivalent with list comprehension (more readable):
result2 = sum(x**2 for x in nums if x % 2 == 0)
print("comprehension:", result2)    # 220 — same!


# ============================================================
#  END OF FILE 5 — ADVANCED FUNCTIONS & ERROR HANDLING
#  You've now completed all 5 files — well done! 🎉
# ============================================================
