# ============================================================
#   🗃️  PYTHON COLLECTIONS — Lists · Tuples · Sets · Dicts
# ============================================================
#   Author  : Md Sourav Oyaj
#   Topics  : Lists · List Comprehension · Tuples
#             Sets · Dictionaries · Dict Comprehension
#   Prerequisite: 01_python_basics.py
# ============================================================
#   QUICK REFERENCE:
#   list  [ ]  → ordered, changeable, allows duplicates
#   tuple ( )  → ordered, UNCHANGEABLE, allows duplicates
#   set   { }  → unordered, no duplicates, no indexing
#   dict  { }  → key:value pairs, ordered (Python 3.7+)
# ============================================================


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 1 — LISTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A list stores multiple items in order.
# Can mix types. Can change, add, and remove items.

# ── Create a list ─────────────────────────────────
list1 = ['abhi', 'kemon', 21, "Ki khobor"]
print(list1)                    # ['abhi', 'kemon', 21, 'Ki khobor']
print(type(list1))              # <class 'list'>

# ── Index access (starts at 0) ────────────────────
print(list1[0])                 # abhi  (first item)
print(list1[2])                 # 21
print(list1[-1])                # Ki khobor  (last item)
print(list1[-2])                # 21 (second from end)

# ── Slicing [start:end]  (end NOT included) ────────
print(list1[0:3])               # ['abhi', 'kemon', 21]
print(list1[1:])                # ['kemon', 21, 'Ki khobor']
print(list1[:2])                # ['abhi', 'kemon']

# ── Add items ─────────────────────────────────────
list1.append("Mango")           # adds to END
print(list1)

list1.insert(0, "Orange")       # inserts at index 0 (shifts rest)
print(list1)

# ── Remove items ──────────────────────────────────
list1.remove("Mango")           # removes by VALUE (first match)
print(list1)

list1.remove(list1[-1])         # remove last item by value
print(list1)

popped = list1.pop()            # removes & returns LAST item
print("Popped:", popped)

popped2 = list1.pop(0)          # removes & returns item at index 0
print("Popped2:", popped2)

# ── Check membership ──────────────────────────────
list1 = ['abhi', 'kemon', 21, "Ki khobor"]

if "abhi" in list1:
    print("Found")
else:
    print("Not Found")

print("kemon" in  list1)        # True
print("Mango" not in list1)     # True

# ── Useful list operations ────────────────────────
print(len(list1))               # length (number of items)
print(list1.count("abhi"))      # how many times 'abhi' appears
print(list1.index("kemon"))     # index position of 'kemon'

nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                     # sort in-place (ascending)
print(nums)
nums.sort(reverse=True)         # sort descending
print(nums)
nums.reverse()                  # reverse the order
print(nums)

# ── Loop through a list ────────────────────────────
list1 = ['abhi', 'kemon', 21, "Ki khobor"]
for x in list1:
    print(x)

print("─" * 30)

# After removing last item
list1.remove(list1[-1])
for x in list1:
    print(x)
print("─" * 30)

# ── Join two lists ─────────────────────────────────
list2 = ['Mango', 'Aam', 'Lichi', 'Lichu', 'Orange', 'Malta']
list3 = ['Kodu', 'Kodu', 'Begun', 'Pumpkin']
list4 = list2 + list3               # join with +
print(list4)
print(type(list4))                  # <class 'list'>

for y in list4:
    print(y)

# list.extend() is another way
list2.extend(["Jackfruit", "Papaya"])
print(list2)

# ── my_list examples from original ───────────────
my_list = ['Apple', 'Mango']
print(my_list[1])               # Mango

my_list.insert(0, 'Orange')     # insert at front
print(my_list)                  # ['Orange', 'Apple', 'Mango']

# ✅ TASK 1: Create a list of 5 subjects. Print the 2nd and last one.
# ✅ TASK 2: Add "AI" to the list, remove the 3rd subject, then sort it.
# ✅ TASK 3: Write a loop that prints only items with more than 4 characters.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 2 — LIST COMPREHENSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A short, elegant way to create lists.
# Syntax: [expression  for item in iterable  if condition]

# Multiplication table of 5 (one line!)
table_5 = [5 * i for i in range(1, 11)]
print(table_5)      # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Squares of 1–10
squares = [x ** 2 for x in range(1, 11)]
print(squares)      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Only even numbers from 1–20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Convert all to uppercase
fruits  = ["apple", "mango", "banana"]
big     = [f.upper() for f in fruits]
print(big)          # ['APPLE', 'MANGO', 'BANANA']

# Get lengths of each word
lens = [len(f) for f in fruits]
print(lens)         # [5, 5, 6]

# Filter: only words longer than 4 chars
long_fruits = [f for f in fruits if len(f) > 4]
print(long_fruits)  # ['apple', 'mango', 'banana']

# Without list comprehension (longer way — same result)
table_5_old = []
for i in range(1, 11):
    table_5_old.append(5 * i)
print(table_5_old)  # same as above

# ✅ TASK 1: Create a list of cubes (n³) for n = 1 to 10.
# ✅ TASK 2: Extract all words that start with a capital letter from:
#            ["Dhaka", "city", "Bangladesh", "river", "Padma"]
# ✅ TASK 3: Create a list of (n, n²) tuples for n = 1 to 5.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 3 — TUPLES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A tuple is like a list but IMMUTABLE (cannot be changed).
# Use tuples for data that should not change.

# ── Create a tuple ────────────────────────────────
tuple1 = ('Mango', 'Aam', 'Lichi', 'Lichu', 'Orange', 'Malta')
print(tuple1)
print(type(tuple1))             # <class 'tuple'>

# Single-value tuple MUST have a trailing comma
single = ('Ngi',)               # ← comma makes it a tuple
not_tuple = ('Ngi')             # ← NO comma: just a string!
print(type(single))             # <class 'tuple'>
print(type(not_tuple))          # <class 'str'>   ← surprise!

# ── Index access — same as list ────────────────────
print(tuple1[0])                # Mango
print(tuple1[-1])               # Malta
print(tuple1[1:4])              # ('Aam', 'Lichi', 'Lichu')

# ── Immutability — you CANNOT change a tuple ──────
# tuple1[0] = 'Jackfruit'       # ← TypeError: 'tuple' object does not support item assignment
# tuple1.append('Papaya')       # ← AttributeError: 'tuple' has no attribute 'append'
# tuple1.remove('Mango')        # ← AttributeError

# ── But you CAN read from it ──────────────────────
print(tuple1.index('Aam'))      # 1  (position)
print(tuple1.count('Lichi'))    # 1  (how many times)
print(len(tuple1))              # 6

# ── Tuple unpacking ────────────────────────────────
# Assign each element to its own variable in one line
coordinates = (10, 20, 30)
a, b, c = coordinates
print(a, b, c)          # 10 20 30  (no parentheses!)
print(coordinates)      # (10, 20, 30)  tuple still intact

# Swap two variables using tuple unpacking (Python trick!)
x, y = 5, 10
x, y = y, x            # swap!
print(x, y)            # 10 5

# ── Tuple in a function ────────────────────────────
# Great for returning multiple values
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 9, 2, 7])
print(f"Min: {lo}, Max: {hi}")      # Min: 1, Max: 9

# ── Loop through a tuple ──────────────────────────
for fruit in tuple1:
    print(fruit)

# ── Why use tuple over list? ──────────────────────
# ✔ Faster than list
# ✔ "Write-protected" — data can't be accidentally changed
# ✔ Can be used as dictionary keys (lists cannot)
# ✔ Makes intent clear: this data is fixed

# ✅ TASK 1: Create a tuple of the 7 days of the week. Print day 3 and 5.
# ✅ TASK 2: Unpack the tuple (10, 20, 30, 40) into four variables and
#            print their sum.
# ✅ TASK 3: Show that trying to change a tuple element raises a TypeError.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 4 — SETS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A set stores UNIQUE items (no duplicates).
# Unordered — no indexing, order not guaranteed.
# Great for membership tests and math operations.

# ── Create a set ──────────────────────────────────
my_set = {'Apple', 'Mango'}
print(my_set)
print(type(my_set))             # <class 'set'>

# Duplicates are automatically removed
a = {3, 32, 2, 5, 6, 2, 3}     # 2 and 3 are duplicated
print(a)                        # {32, 2, 3, 5, 6}  ← only unique

# ── No index access ───────────────────────────────
# print(my_set[1])              # ← TypeError: 'set' object is not subscriptable

# ── Membership check (very fast!) ─────────────────
print("Apple" in my_set)        # True
print("Banana" in my_set)       # False

# ── Add / Remove ──────────────────────────────────
my_set.add("Banana")
print(my_set)

my_set.discard("Mango")         # removes if exists; no error if not
my_set.discard("NotHere")       # no error!
print(my_set)

my_set.remove("Apple")          # removes — raises KeyError if not found
print(my_set)

# ── Set math operations ────────────────────────────
a = {3, 32, 2, 5, 6}
b = {3, 5, 2, 90, 867, 6}

# union: all items from both (no duplicates)
c = a.union(b)
print("Union       :", c)               # {2, 3, 32, 5, 6, 867, 90}

# intersection: only items in BOTH
d = a.intersection(b)
print("Intersection:", d)               # {2, 3, 5, 6}

# difference: items in a but NOT in b
e = a.difference(b)
print("Difference a-b:", e)             # {32}

# difference the other way
f = b.difference(a)
print("Difference b-a:", f)             # {867, 90}

# symmetric_difference: items in either but NOT both
g = a.symmetric_difference(b)
print("Sym Diff    :", g)               # {32, 867, 90}

# Operator shortcuts
print(a | b)                    # union
print(a & b)                    # intersection
print(a - b)                    # difference

# ── Remove duplicates from a list using a set ─────
list_with_dups = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(list_with_dups))
print(unique)                   # [1, 2, 3, 4]  (order may vary)

# ── frozenset: immutable set ───────────────────────
fs = frozenset({1, 2, 3})
print(fs)
# fs.add(4)                     # ← AttributeError: frozenset has no add

# ✅ TASK 1: Given two sets of students who passed math and science,
#            find who passed BOTH, who passed only math, and who passed either.
# ✅ TASK 2: Remove duplicates from [1,1,2,3,3,4,5,5,5] using a set.
# ✅ TASK 3: Check if {2, 3} is a subset of {1, 2, 3, 4, 5} using issubset().


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 5 — DICTIONARIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A dictionary stores key:value pairs.
# Keys must be unique. Values can be any type.

# ── Create a dictionary ───────────────────────────
student = {
    'name': 'captrox',
    'age':   24,
    'dept':  'cse'
}
print(student)
print(type(student))            # <class 'dict'>

# ── Access a value by key ─────────────────────────
print(student['name'])          # captrox
print(student['age'])           # 24
print(student.get('dept'))      # cse
print(student.get('gpa', 'N/A'))    # N/A  ← .get() with default (no crash)
# print(student['gpa'])         # ← KeyError if key doesn't exist!

# ── Add / Update items ────────────────────────────
student['add'] = 'akbarshah'    # adds new key
print(student)

student['age'] = 25             # updates existing key
print(student)

# ── Remove items ──────────────────────────────────
del student['add']
print(student)

removed = student.pop('age')    # removes and returns value
print("Removed:", removed)
print(student)

# ── Keys, Values, Items ───────────────────────────
marks = {
    "Abhi": 23,
    "Oyaj": 23,
    "MD":   43
}
print(marks)
print(marks["Abhi"])            # 23
print(marks.keys())             # dict_keys(['Abhi', 'Oyaj', 'MD'])
print(marks.values())           # dict_values([23, 23, 43])
print(marks.items())            # dict_items([('Abhi', 23), ('Oyaj', 23), ('MD', 43)])

# ── Loop through a dictionary ─────────────────────
for key in marks:
    print(key, ":", marks[key])

for key, val in marks.items():
    print(f"{key} scored {val}")

# ── Check membership ──────────────────────────────
print("Abhi" in marks)          # True  (checks KEYS by default)
print(23 in marks.values())     # True  (check values)

# ── Nested dictionary ─────────────────────────────
school = {
    "student1": {"name": "Sourav", "age": 23},
    "student2": {"name": "Tanvir", "age": 22},
}
print(school["student1"]["name"])       # Sourav
print(school["student2"]["age"])        # 22

# ── update() merges another dict ──────────────────
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
d1.update(d2)               # d2 overwrites d1's 'b'
print(d1)                   # {'a': 1, 'b': 99, 'c': 3}

# ── Practical: Playlist (dict of list) ───────────
playlist = {"Favourites": ["Song A", "Song B"]}
playlist["Favourites"].append("Song C")
print(playlist)

# ✅ TASK 1: Create a dict of 3 countries with their capitals. Print all pairs.
# ✅ TASK 2: Add a new country, update an existing capital, then remove one entry.
# ✅ TASK 3: Write a loop that prints only students with marks >= 30.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 6 — DICT COMPREHENSION & COMBINED USAGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Syntax: {key_expr: val_expr  for item in iterable  if condition}

# Multiplication table of 5 as a dict  {n: 5×n}
times_5 = {i: 5 * i for i in range(1, 11)}
print(times_5)
# {1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}

# Squares dict
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)              # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists (zip)
names  = ["Sourav", "Abhi", "Tanvir"]
scores = [90,        85,     78]
grade_book = {n: s for n, s in zip(names, scores)}
print(grade_book)           # {'Sourav': 90, 'Abhi': 85, 'Tanvir': 78}

# With filter: only students who passed (>=80)
passed = {n: s for n, s in grade_book.items() if s >= 80}
print(passed)               # {'Sourav': 90, 'Abhi': 85}

# ── Full comparison: list vs tuple vs set vs dict ─
print("\n─── All four types together ───")
my_list  = ['Apple', 'Mango']               # [ ] ordered, changeable
my_tuple = ('Apple', 'Mango')               # ( ) ordered, locked
my_set   = {'Apple', 'Mango'}               # { } unordered, unique
my_dict  = {'fruit1': 'Apple',
             'fruit2': 'Mango'}             # {k:v} key-value

print(my_list[1])           # Mango  ← index works
print(my_tuple[1])          # Mango  ← index works
# print(my_set[1])          # ← TypeError: no indexing on sets!
print(my_dict['fruit2'])    # Mango  ← key access

my_list.insert(0, 'Orange')
print(my_list)              # ['Orange', 'Apple', 'Mango']

# my_tuple.index('Apple')  → just finds index, doesn't change tuple
print(my_tuple.index('Apple'))  # 0

print("Set:", my_set)           # unordered — could be {'Mango', 'Apple'}

# ── When to use which? ────────────────────────────
# list   → ordered collection, frequently modified
# tuple  → fixed/constant data (coordinates, RGB colors, DB row)
# set    → unique items, fast membership tests, math operations
# dict   → lookup by name/key (config, JSON-like data, counters)

# ✅ TASK 1: Use dict comprehension to make {word: len(word)} from a word list.
# ✅ TASK 2: Filter a dict to keep only key-value pairs where value > 50.
# ✅ TASK 3: Use a set comprehension to get unique first letters from a word list.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  BONUS — PLAYLIST CLASS  (from your original code)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A practical use of lists inside a class.
# (Full OOP coverage is in 03_python_oop.py)

class Playlist:
    def __init__(self, name):
        self.name  = name
        self.songs = []                 # list starts empty

    def add_song(self, song):
        self.songs.append(song)
        print(f"Song '{song}' Added Successfully")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Song '{song}' Removed Successfully")
        else:
            print(f"Song '{song}' Not Found")

    def show_songs(self):
        print(f"\nPlaylist: {self.name}")
        for song in self.songs:
            print(f"  - {song}")

my_playlist = Playlist("Favourites")
my_playlist.add_song("Sagorer Tir theke")
my_playlist.add_song("Sajni re")
my_playlist.add_song("Ei Raat Tomar Amar")
my_playlist.show_songs()
my_playlist.remove_song("Sajni re")
my_playlist.remove_song("Abcd")         # not in list
my_playlist.show_songs()

# ✅ TASK: Extend the Playlist class:
#   1. Add a method show_count() that prints how many songs are in the list.
#   2. Add a method has_song(song) that returns True/False.
#   3. Add a method clear_playlist() that removes all songs.


# ============================================================
#  END OF FILE 2 — PYTHON COLLECTIONS
#  Next: 03_python_oop.py  →  Classes, Inheritance, OOP
# ============================================================
