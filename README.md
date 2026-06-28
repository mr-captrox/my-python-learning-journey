# 🐍 Python Learning Journey — From Zero to Infinity

> *"Every expert was once a beginner. Every pro was once an amateur."*

This repository is my personal, organized record of learning Python from scratch.
I wrote these files as I studied — adding examples, explanations, common mistakes, and hands-on tasks — so that **anyone who picks them up can follow the same journey I took.**

If you're learning Python, clone this, open it in VSCode, and run the cells one by one. Everything is explained right there in the code.

---

## 👤 About the Author

**Md Sourav Oyaj** — CS student, passionate about programming and problem solving.
I built this as a structured reference for myself and anyone else starting out with Python.

---

## 📁 What's Inside

| File | Topics Covered | Lines |
|------|---------------|-------|
| [`01_python_basics.py`](./01_python_basics.py) | Output, Variables, Data Types, Casting, Strings, Booleans, Operators, if/elif/else, match/case, While Loops, For Loops, Functions, Lambda, Recursion, Input, Try/Except, Math, JSON | ~1000 |
| [`02_python_collections.py`](./02_python_collections.py) | Lists, List Comprehension, Tuples, Sets, Dictionaries, Dict Comprehension, Practical Class Example | ~500 |
| [`03_python_oop.py`](./03_python_oop.py) | Classes & Objects, `__init__` & `self`, Class vs Instance Attributes, `__str__`, Inheritance, Polymorphism, Encapsulation, Operator Overloading, Inner Classes | ~745 |
| [`04_advanced_oop.py`](./04_advanced_oop.py) | `__repr__` vs `__str__`, `@staticmethod`, `@classmethod` | ~472 |
| [`05_advanced_functions.py`](./05_advanced_functions.py) | `raise`, `try/except/finally`, `while True` + `try/except`, `map()`, `filter()`, `reduce()`, Walrus Operator `:=`, `*args`, `**kwargs` | ~831 |
| [`06_python_file_handling_and_modules.py`](./06_python_file_handling_and_modules.py) | File Handling (`open`, `read`, `write`, `append`, `with`), `os` module, `shutil` module, `argparse` module, `re` (Regex) module | ~788 |

---

## 🗺️ Learning Roadmap

```
01_python_basics.py
│
├── Section 1  — Hello World & print()
├── Section 2  — Variables & Data Types
├── Section 3  — Type Casting
├── Section 4  — Strings (Deep Dive)
├── Section 5  — String Formatting (f-strings, .format())
├── Section 6  — Booleans & Comparisons
├── Section 7  — Operators (arithmetic, assignment)
├── Section 8  — if / elif / else
├── Section 9  — match / case  (Python 3.10+)
├── Section 10 — While Loops
├── Section 11 — For Loops & range()
├── Section 12 — Functions (parameters, return, *args, defaults)
├── Section 13 — Lambda, map(), filter()
├── Section 14 — Recursion (fibonacci, factorial)
├── Section 15 — User Input
├── Section 16 — Try / Except (Error Handling)
├── Section 17 — Math Module
└── Section 18 — JSON Module

02_python_collections.py
│
├── Section 1  — Lists (CRUD, sorting, looping)
├── Section 2  — List Comprehension
├── Section 3  — Tuples (immutability, unpacking)
├── Section 4  — Sets (union, intersection, difference)
├── Section 5  — Dictionaries (CRUD, nested dicts)
├── Section 6  — Dict Comprehension & All-4 Comparison
└── Bonus      — Playlist Class (practical example)

03_python_oop.py
│
├── Section 1  — Classes & Objects
├── Section 2  — __init__ & self
├── Section 3  — Class Properties (add/delete)
├── Section 4  — __str__ (string representation)
├── Section 5  — Inheritance & super()
├── Section 6  — Polymorphism & Duck Typing
├── Section 7  — Encapsulation (public/protected/private, @property)
├── Section 8  — Operator Overloading (__add__, __sub__, __eq__, ...)
├── Section 9  — Inner / Nested Classes
└── Section 10 — Full Capstone: all OOP concepts together

04_advanced_oop.py
│
├── Section 1  — __str__ vs __repr__
├── Section 2  — @staticmethod
├── Section 3  — @classmethod
└── Section 4  — Full Employee Class (All Together)

05_advanced_functions.py
│
├── Section 1  — raise (Manually Throwing Exceptions)
├── Section 2  — try / except / finally (Advanced)
├── Section 3  — while True + try/except (Safe Input Loop)
├── Section 4  — map() (Apply function to every item)
├── Section 5  — filter() (Keep only matching items)
├── Section 6  — reduce() (Combine all items into one)
├── Section 7  — Walrus Operator := (Python 3.8+)
├── Section 8  — *args (Variable Positional Arguments)
├── Section 9  — **kwargs (Variable Keyword Arguments)
├── Section 10 — *args + **kwargs (Combined)
└── Bonus      — All Functional Tools Side by Side

06_python_file_handling_and_modules.py
│
├── Section 1  — File Modes Reference
├── Section 2  — Writing Files (create & write)
├── Section 3  — Reading Files
├── Section 4  — Appending to Files
├── Section 5  — The with Statement (Context Manager)
├── Section 6  — Error Handling with Files
├── Section 7  — os Module (Operating System Interface)
├── Section 8  — shutil Module (Shell Utilities)
├── Section 9  — argparse Module (Command-Line Arguments)
├── Section 10 — re Module (Regular Expressions)
└── Section 11 — Final Cleanup
```

---

## 🚀 How to Use These Files

### Option 1 — Interactive (Recommended) 🌟
1. Open the file in **VSCode**
2. Install the **Jupyter** extension if you haven't already
3. Right-click inside the file → **"Run in Interactive Window"**
4. Each `# %%` block is a **separate cell** — run them one by one and see the output immediately

### Option 2 — Run from Terminal
```bash
python 01_python_basics.py
python 02_python_collections.py
python 03_python_oop.py
```

### Option 3 — Jupyter Notebook
Convert any file to a notebook:
```bash
pip install jupytext
jupytext --to notebook 01_python_basics.py
```

> **Prerequisite:** Python 3.10+ (for `match/case` in File 1). Everything else works on 3.8+.

---

## 💡 What Makes These Files Different

Most tutorials just show you *what* works. These files show you **both sides**:

```python
# ✅ This works:
d = str(12)
print(d + "12")        # "1212"  ← string joining

# ❌ This breaks (and WHY):
# print("Age: " + 23)  # TypeError! Can't join str and int
print("Age: " + str(23))  # ✅ Fix: cast first
```

Every section includes:
- 📖 **Clear explanation** of the concept
- 💻 **Working examples** with expected output in comments
- ⚠️ **Common mistakes** and why they cause errors
- ✅ **Practice tasks** at the end of each section to test your understanding

---

## ✅ Practice Tasks (Highlights)

Each section ends with tasks. Here's a taste of what you'll practice:

**Basics**
- Build a grade calculator with `if/elif/else`
- Write a recursive Fibonacci and Factorial function
- Handle `ValueError`, `ZeroDivisionError`, `IndexError` with try/except
- Parse and pretty-print JSON data

**Collections**
- Create list comprehensions, filter, and transform data in one line
- Perform set operations: union, intersection, difference on real data
- Build nested dictionaries and loop over them
- Design and extend a `Playlist` class using lists

**OOP**
- Implement a `BankAccount` with private balance and validated deposit/withdraw
- Build a class hierarchy: `Vehicle → Car / Boat / Plane` with polymorphic `move()`
- Use `@property` for clean getter/setter without boilerplate
- Overload `+`, `-`, `*`, `==` for a custom `Point` class
- Final capstone: build a complete **Animal Shelter** system from scratch

**Advanced Topics**
- Build robust input validation loops with `try/except` and `raise`
- Clean up data using functional tools: `map()`, `filter()`, and `reduce()`
- Use the Walrus operator `:=` for cleaner and more efficient code
- Create flexible functions with `*args` and `**kwargs`
- Understand the difference between `__str__` and `__repr__`
- Use `@classmethod` as alternative constructors and `@staticmethod` for utilities

**File Handling & Modules**
- Read, write, and safely append to files using context managers (`with`)
- Automate file and folder management using `os` and `shutil`
- Build a fully functional Command Line Interface (CLI) tool with `argparse`
- Master text manipulation and validation with Regular Expressions (`re`)

---

## 📌 Quick Reference Card

```
STRINGS        → str, len(), slicing, split(), join(), f-strings
NUMBERS        → int, float, math module, round()
BOOLEAN LOGIC  → and, or, not, comparison operators
CONTAINERS     → list[], tuple(), set{}, dict{key:val}
FLOW CONTROL   → if/elif/else, match/case, for, while, break, continue
FUNCTIONS      → def, return, *args, default params, lambda
ERROR HANDLING → try/except/else/finally
OOP            → class, __init__, self, inheritance, @property
```

---

## 🛠️ Requirements

- Python **3.10+**
- No external libraries needed (only built-in `math` and `json` modules)
- VSCode + Jupyter extension (for interactive cell execution)

---

## 🌱 My Journey & Motivation

I started learning Python and quickly realized that just watching tutorials wasn't enough — I needed to **write things down, experiment, and break things on purpose** to truly understand.

So I created these files as a living notebook:
- I ran every single line to verify it works
- I noted every error I encountered (and why it happens)
- I added tasks so I could test myself — and so *you* can test yourself too

This isn't a polished textbook. It's **real notes from a real learner**, organized so anyone can pick up where they left off.

If you're learning Python, I hope this saves you hours of confusion and gives you a clear, structured path to follow. ⭐

---

## 📬 Connect

If you find this helpful, feel free to **star ⭐ the repo** — it motivates me to keep sharing what I learn!

**Md Sourav Oyaj**
- GitHub: [@captrox](https://github.com/mr-captrox)

---

<p align="center">
  <b>Happy Coding! 🐍</b><br>
  <i>Start with File 1 → master the basics → move to Collections → conquer OOP → explore Advanced Topics → dive into Modules & Regex</i>
</p>
