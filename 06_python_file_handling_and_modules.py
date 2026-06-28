# ============================================================
#   📂  PYTHON MODULES & STANDARD LIBRARY
# ============================================================
#   Author  : Md Sourav Oyaj
#   Topics  : File Handling (open, read, write, append, with)
#             os Module (navigate, list, check, delete dirs)
#             shutil Module (copy, move, delete folder trees)
#             argparse Module (CLI arguments)
#             re Module (Regular Expressions)
#   Prerequisite: 01_python_basics.py, 05_advanced_functions.py
# ============================================================
#   HOW TO USE:
#   ▸ Open in VSCode → right-click → "Run in Interactive Window"
#   ▸ Each # %% block is one Jupyter cell — run them one by one
#   ▸ ⚠️  Sections 1–8 create / read / delete real files on disk.
#          Run them in order — each section sets up what the next needs.
# ============================================================


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 1 — FILE MODES REFERENCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Before opening a file you must tell Python HOW to open it.
# The second argument to open() is the MODE.
#
#  MODE   MEANING                              FILE EXISTS?  FILE MISSING?
#  ─────────────────────────────────────────────────────────────────────
#  "r"  → Read only (default)                 opens fine    FileNotFoundError
#  "w"  → Write (OVERWRITES everything!)      opens & clears creates new file
#  "a"  → Append (adds to end)                opens fine    creates new file
#  "x"  → Create new (exclusive)             FileExistsError creates new file
#  ─────────────────────────────────────────────────────────────────────
#  ADD "b" for BINARY mode (images, PDFs, audio)
#  "rb" → read binary | "wb" → write binary
#  ─────────────────────────────────────────────────────────────────────
#
#  ⚠️  Common trap with "w" mode:
#      If the file already has content, "w" DELETES it all first.
#      Use "a" if you want to ADD to an existing file.

print("File modes: 'r', 'w', 'a', 'x'  (add 'b' for binary)")
print("Text mode: default | Binary mode: add 'b'  e.g. 'rb', 'wb'")


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 2 — WRITING FILES  (create & write)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# We write FIRST so the file exists when we try to read it below.

# ── 2.1 write() — basic write ────────────────────
# "w" creates the file if it doesn't exist.
# "w" WIPES existing content — treat it like "overwrite".
f = open("msg.txt", "w")
f.write("Hello from Python!\n")
f.write("This is line 2.\n")
f.write("Sourav wrote this file.\n")
f.close()                           # ⚠️ ALWAYS close what you open!
                                    # open file = locked resource on disk
print("msg.txt created ✅")

# ── 2.2 write() with multiline string ────────────
# You can also write a big block at once using triple quotes.
f = open("sourav.txt", "w")
content = """Name: Md Sourav Oyaj
Dept: Computer Science
Sem : 7
CGPA: 3.75
City: Dhaka, Bangladesh
"""
f.write(content)
f.close()
print("sourav.txt created ✅")

# ── 2.3 writelines() — write a list of lines ─────
lines = [
    "Mango\n",
    "Lichi\n",
    "Orange\n",
    "Jackfruit\n",
]
f = open("fruits.txt", "w")
f.writelines(lines)                 # writes each element, no auto newline
f.close()
print("fruits.txt created ✅")

# ✅ TASK 1: Create a file called "info.txt" and write your name,
#            age, and favourite language in it (one per line).
# ✅ TASK 2: What happens if you open the same file with "w" TWICE?
#            Try it — write something, then write again. Check the file.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 3 — READING FILES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Three ways to read: read(), readline(), readlines() + loop.

# ── 3.1 read() — whole file as one big string ────
f = open("msg.txt", "r")           # "r" is the default, can omit
content = f.read()
print(content)
print(type(content))               # <class 'str'>
f.close()

# ── 3.2 read(n) — read only n characters ─────────
f = open("msg.txt", "r")
chunk = f.read(10)                 # first 10 characters only
print(repr(chunk))                 # repr() shows \n explicitly
f.close()

# ── 3.3 readline() — one line at a time ──────────
# Useful when you process lines one by one (huge files, log parsing)
f = open("msg.txt", "r")
line1 = f.readline()              # reads up to and INCLUDING \n
line2 = f.readline()
print(line1, end="")              # end="" avoids double newline
print(line2, end="")
f.close()

# ── 3.4 readlines() — all lines as a list ─────────
f = open("msg.txt", "r")
all_lines = f.readlines()         # ['Hello from Python!\n', 'This is line 2.\n', ...]
print(all_lines)
print(all_lines[0])               # first line
print(all_lines[-1])              # last line
f.close()

# ── 3.5 Loop line by line (most memory-efficient) ─
# For large files this is the best approach — no entire file in RAM.
f = open("msg.txt", "r")
for line in f:
    print(line, end="")           # line already has \n, so end=""
f.close()

# ✅ TASK 1: Open "sourav.txt" and print only lines that contain "Name".
# ✅ TASK 2: Open "fruits.txt" and print how many lines (fruits) it has.
# ✅ TASK 3: Open "msg.txt" and print it in UPPERCASE.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 4 — APPENDING TO FILES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# "a" mode adds content to the END of the file.
# It does NOT delete existing content (unlike "w").
# If the file doesn't exist yet, it creates a new one.

# ── 4.1 Append a single line ─────────────────────
f = open("fruits.txt", "a")
f.write("Guava\n")                # adds to the end
f.close()

# Verify it was appended
f = open("fruits.txt", "r")
print(f.read())
f.close()

# ── 4.2 Append multiple lines ────────────────────
extra = ["Banana\n", "Papaya\n"]
f = open("fruits.txt", "a")
f.writelines(extra)
f.close()

# Read back to confirm
f = open("fruits.txt", "r")
for line in f:
    print(line, end="")
f.close()

# ── 4.3 Append user input (demo with hardcoded value) ──
# In a real script you'd use: text = input("Enter text: ")
# Here we simulate it so the interactive window doesn't block.
text = "Pineapple\n"               # pretend this came from input()
f = open("fruits.txt", "a")
f.write(text)
f.close()
print("Added:", text.strip())

# ✅ TASK: Open "sourav.txt" and append "Status: Active" to the end.
#          Then read the whole file to confirm.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 5 — THE with STATEMENT  (Context Manager)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Using f.close() manually is error-prone — if an exception
# happens BEFORE close(), the file stays open (resource leak).
#
# The with statement fixes this:
# ✅ Automatically closes the file when the block exits.
# ✅ Even closes it if an exception is raised inside.
# ✅ Cleaner, shorter, and considered best practice.
#
# Syntax:
#   with open("file.txt", "mode") as f:
#       # use f here
#   # file is automatically closed here, no f.close() needed

# ── 5.1 Read with 'with' ─────────────────────────
with open("msg.txt", "r") as f:
    c = f.read()
    print(c)
# f is now closed — no need for f.close()

# ── 5.2 Write with 'with' ────────────────────────
with open("notes.txt", "w") as f:
    f.write("Python is fun!\n")
    f.write("with statement closes files safely.\n")
print("notes.txt written ✅")

# ── 5.3 Read line by line with 'with' ────────────
with open("sourav.txt", "r") as f:
    for line in f:
        print(line, end="")

# ── 5.4 Open multiple files at once ──────────────
# with can manage more than one file simultaneously
with open("msg.txt", "r") as src, open("msg_copy.txt", "w") as dst:
    dst.write(src.read())          # copy one file to another!
print("msg.txt copied to msg_copy.txt ✅")

# ── 5.5 Old way vs new way comparison ────────────
# ❌ Old (risky — close might never run if error occurs):
# f = open("file.txt", "r")
# content = f.read()
# f.close()

# ✅ New (safe — closes even if error occurs):
# with open("file.txt", "r") as f:
#     content = f.read()

# ✅ TASK 1: Use 'with' to create "poem.txt" and write 3 lines of a poem.
#            Then use another 'with' block to read and print it.
# ✅ TASK 2: Use the two-file 'with' trick to copy "fruits.txt" to "fruits_backup.txt".


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 6 — ERROR HANDLING WITH FILES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Files fail for many reasons:
#   FileNotFoundError → the file doesn't exist
#   PermissionError   → you don't have read/write access
#   IsADirectoryError → you tried to open a folder as a file

# ── 6.1 Catch FileNotFoundError ──────────────────
try:
    f = open("ghost.txt", "r")    # this file doesn't exist
    for line in f:
        print(line)
except FileNotFoundError:
    print("❌ File not found!")

# ── 6.2 Catch multiple file-related errors ────────
def safe_read(path):
    """Safely reads a file and returns its content, or None on error."""
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ '{path}' does not exist.")
    except PermissionError:
        print(f"❌ No permission to read '{path}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return None

result = safe_read("msg.txt")       # exists → prints content
print(result)

result = safe_read("ghost.txt")     # doesn't exist → handled
print(result)                       # None

# ── 6.3 "x" mode — create new, error if exists ───
# Useful when you need a FRESH file and don't want to accidentally
# overwrite something important.
try:
    with open("unique.txt", "x") as f:
        f.write("This file was just created!")
    print("unique.txt created ✅")
except FileExistsError:
    print("❌ unique.txt already exists — not overwriting it!")

# ── 6.4 with + try/except together ───────────────
# This is the complete, production-quality pattern:
def write_safe(path, text):
    try:
        with open(path, "w") as f:
            f.write(text)
        print(f"✅ Wrote to '{path}'")
    except PermissionError:
        print(f"❌ Cannot write to '{path}' — permission denied")

write_safe("output.txt", "Hello, world!")

# ✅ TASK 1: Write a function read_first_line(path) that returns the first
#            line of a file, or an error message if the file doesn't exist.
# ✅ TASK 2: Write a function that appends to a log file and creates it if
#            it doesn't exist. (Hint: "a" mode creates the file if missing.)


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 7 — os MODULE  (Operating System Interface)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# The os module lets Python talk to the operating system:
# navigate directories, check paths, rename and delete files.

import os

# ── 7.1 Current directory ────────────────────────
cwd = os.getcwd()
print("Current working directory:", cwd)

# ── 7.2 List files/folders in a directory ─────────
items = os.listdir(".")            # "." means current folder
print("Files in current dir:", items)

# ── 7.3 Check if a path exists ───────────────────
print(os.path.exists("msg.txt"))   # True  — we created it earlier
print(os.path.exists("ghost.txt")) # False — never created

# ── 7.4 Check if it's a file or a folder ──────────
print(os.path.isfile("msg.txt"))   # True
print(os.path.isdir("."))          # True  — "." is the current dir

# ── 7.5 Join paths safely ────────────────────────
# NEVER build paths with string + — it breaks on Windows vs Linux
# ❌ Bad:  "folder" + "/" + "file.txt"
# ✅ Good: os.path.join("folder", "file.txt")
path = os.path.join("subfolder", "data.txt")
print("Safe path:", path)          # subfolder/data.txt  (or subfolder\data.txt on Windows)

# ── 7.6 File info ────────────────────────────────
size  = os.path.getsize("msg.txt")       # size in bytes
print(f"msg.txt size: {size} bytes")

# ── 7.7 Rename a file ────────────────────────────
os.rename("notes.txt", "renamed_notes.txt")
print("notes.txt  →  renamed_notes.txt ✅")

# ── 7.8 Create and remove directories ─────────────
os.mkdir("test_folder")                   # create one folder
print("test_folder created ✅")
print(os.path.exists("test_folder"))      # True

os.rmdir("test_folder")                   # remove it (only works if EMPTY)
print("test_folder removed ✅")
print(os.path.exists("test_folder"))      # False

# ── 7.9 Create nested directories ────────────────
os.makedirs("parent/child/grandchild", exist_ok=True)
# exist_ok=True → no error if folders already exist
print("Nested dirs created ✅")

# ── 7.10 Delete files ─────────────────────────────
# ⚠️ os.remove() is PERMANENT — no recycle bin!
os.remove("output.txt")           # delete output.txt
print("output.txt removed ✅")

# ── 7.11 Walk a directory tree ────────────────────
# os.walk() visits every folder/subfolder under a root path.
# (Useful for finding all .txt files recursively, etc.)
for root, dirs, files in os.walk("parent"):
    print(f"📂 {root}")
    for fname in files:
        print(f"   📄 {fname}")
    for dname in dirs:
        print(f"   📁 {dname}")

# ✅ TASK 1: Write a function that lists ONLY .txt files in the current folder.
#            (Hint: loop os.listdir() and check if name.endswith(".txt"))
# ✅ TASK 2: Write a function that prints the total size (in bytes) of all
#            files in the current directory.
# ✅ TASK 3: Check if a given path is a file, directory, or doesn't exist —
#            and print a suitable message for each case.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 8 — shutil MODULE  (Shell Utilities)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# shutil goes beyond os — it handles ENTIRE FOLDERS:
# copying trees, moving files, deleting non-empty directories.
#
# os         → works on single files / empty dirs
# shutil     → works on entire directory trees

import shutil

# ── 8.1 Copy a file ───────────────────────────────
# shutil.copy("source", "destination")
# → copies the file content and permissions
shutil.copy("msg.txt", "msg_backup.txt")
print("msg.txt  →  msg_backup.txt ✅")

# shutil.copy2("source", "destination")
# → same as copy but ALSO preserves timestamps (metadata)
shutil.copy2("sourav.txt", "sourav_backup.txt")
print("sourav.txt  →  sourav_backup.txt (with metadata) ✅")

# ── 8.2 Copy an entire directory ──────────────────
# shutil.copytree("src_dir", "dst_dir")
# dst_dir must NOT already exist — shutil creates it
if not os.path.exists("parent_backup"):
    shutil.copytree("parent", "parent_backup")
    print("parent/  →  parent_backup/ ✅")

# ── 8.3 Move a file or folder ─────────────────────
# Works like mv in Linux — can also rename!
shutil.move("renamed_notes.txt", "archived_notes.txt")
print("renamed_notes.txt  →  archived_notes.txt ✅")

# ── 8.4 Delete a whole directory tree ─────────────
# ⚠️  shutil.rmtree() is PERMANENT — no recycle bin, no undo!
# os.rmdir() only removes EMPTY folders.
# shutil.rmtree() removes a folder AND everything inside it.
shutil.rmtree("parent")
print("parent/ (and all contents) removed ✅")
shutil.rmtree("parent_backup")
print("parent_backup/ removed ✅")

# ── 8.5 Disk usage ────────────────────────────────
# shutil.disk_usage() returns total, used, and free disk space
usage = shutil.disk_usage(".")
print(f"Total: {usage.total // (1024**3)} GB")
print(f"Used : {usage.used  // (1024**3)} GB")
print(f"Free : {usage.free  // (1024**3)} GB")

# ── 8.6 os vs shutil comparison ──────────────────
#  TASK            USE
#  ─────────────────────────────────────────────
#  Delete file      os.remove("file.txt")
#  Delete empty dir os.rmdir("dir/")
#  Delete full dir  shutil.rmtree("dir/")      ← shutil needed
#  Copy file        shutil.copy("src","dst")   ← shutil needed
#  Copy dir tree    shutil.copytree("s","d")   ← shutil needed
#  Move file/dir    shutil.move("src","dst")   ← shutil needed
#  List dir         os.listdir(".")
#  Current dir      os.getcwd()
#  Join paths       os.path.join("a","b")

# Cleanup files we no longer need
for fname in ["msg_backup.txt", "sourav_backup.txt",
              "archived_notes.txt", "msg_copy.txt",
              "unique.txt", "fruits_backup.txt"]:
    if os.path.exists(fname):
        os.remove(fname)
print("Cleanup done ✅")

# ✅ TASK 1: Write a function backup(src_file) that copies a file to
#            a "backups/" folder (creating the folder if it doesn't exist).
# ✅ TASK 2: Write a function purge_folder(path) that deletes a folder
#            safely — checking it exists before calling rmtree().
# ✅ TASK 3: Print disk usage in human-readable GB/MB format.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 9 — argparse MODULE  (Command-Line Arguments)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# argparse lets your script accept arguments from the terminal:
#   python calculator.py 10 5 add   →  The result is 15.0
#
# ⚠️  argparse ONLY works when you run from the TERMINAL.
#     It does NOT work inside Jupyter / Interactive Window
#     because there's no command-line to read from.
#
# This section explains the concept with runnable demo code,
# and shows the real argparse code in comments so you can
# copy it to a standalone .py file and run it with python.
#
# ── Concept: sys.argv ─────────────────────────────
# Every Python script receives its arguments via sys.argv list.
import sys

# If you ran: python script.py hello world 42
# Then sys.argv = ["script.py", "hello", "world", "42"]
print("This script name:", sys.argv[0])
# sys.argv[1], [2], ... are the arguments the user typed.
# argparse is a friendlier wrapper around sys.argv.

# ── Simulated demo (no real terminal needed) ──────
class FakeArgs:
    """Simulates what argparse.parse_args() returns."""
    num1       = 10.0
    num2       = 5.0
    Operations = "add"

args = FakeArgs()

def run_calculator(args):
    """Runs the calculator using parsed arguments."""
    print(f"num1={args.num1}, num2={args.num2}, op={args.Operations}")
    if args.Operations == "add":
        print(f"The result is {args.num1 + args.num2}")
    elif args.Operations == "sub":
        print(f"The result is {args.num1 - args.num2}")
    elif args.Operations == "mul":
        print(f"The result is {args.num1 * args.num2}")
    elif args.Operations == "div":
        if args.num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"The result is {args.num1 / args.num2}")

run_calculator(args)      # demo: 10 + 5 = 15.0

# ── Real argparse code (run this as a standalone .py) ────
# ─────────────────────────────────────────────────────────
# Copy this block to a new file called  calculator.py
# and run it with:
#   python calculator.py 10 5 add
#   python calculator.py 20 4 div
#   python calculator.py --help          ← auto-generated help!
# ─────────────────────────────────────────────────────────
#
# import argparse
#
# parser = argparse.ArgumentParser(description="Simple Calculator")
#
# # Positional arguments — REQUIRED, must be provided in order
# parser.add_argument("num1",       type=float, help="First number")
# parser.add_argument("num2",       type=float, help="Second number")
# parser.add_argument("Operations", type=str,
#                     choices=["add", "sub", "mul", "div"],
#                     help="Operation to perform")
#
# args = parser.parse_args()
# print(args)                             # Namespace(num1=10.0, num2=5.0, ...)
#
# if   args.Operations == "add": print(f"Result: {args.num1 + args.num2}")
# elif args.Operations == "sub": print(f"Result: {args.num1 - args.num2}")
# elif args.Operations == "mul": print(f"Result: {args.num1 * args.num2}")
# elif args.Operations == "div": print(f"Result: {args.num1 / args.num2}")
# ─────────────────────────────────────────────────────────

# ── Optional arguments with -- prefix ────────────
# Optional arguments are NOT required. They have defaults.
#
# parser.add_argument("--verbose", action="store_true",
#                     help="Print extra info")
# parser.add_argument("--output",  type=str, default="result.txt",
#                     help="Output file name")
#
# Usage:
#   python script.py 10 5 add --verbose
#   python script.py 10 5 add --output answer.txt

# ── Short flags (-v instead of --verbose) ─────────
# parser.add_argument("-v", "--verbose", action="store_true")
# Usage: python script.py 10 5 add -v

# ── add_argument options cheat-sheet ──────────────
#
#  OPTION          MEANING                         EXAMPLE
#  ──────────────────────────────────────────────────────────
#  type=float      convert arg to float            type=int, type=str
#  help="..."      description shown in --help
#  default=X       value if arg is not supplied    default=0
#  choices=[...]   restrict to allowed values      choices=["a","b"]
#  action="store_true"  flag that sets True/False  --verbose
#  required=True   force an optional arg to exist

print("\n📌 argparse works in the terminal — see comments above for real code.")
print("   Run:  python calculator.py 10 5 add")

# ✅ TASK 1: Create calculator.py from the commented code above.
#            Run it in your terminal with different operations.
# ✅ TASK 2: Add a "--round" optional flag that rounds the result to 2 decimals.
# ✅ TASK 3: Add a "--verbose" flag that prints extra info (operands, operation).


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 10 — re MODULE  (Regular Expressions)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A regular expression (regex) is a PATTERN that describes text.
# The re module lets you search, find, replace, and split strings
# using those patterns — far more powerful than str.find().
#
# Core functions:
#   re.search(pattern, text)       → first match anywhere in text
#   re.findall(pattern, text)      → list of all matches
#   re.sub(pattern, replacement, text) → replace matches
#   re.match(pattern, text)        → match at START of text only
#   re.split(pattern, text)        → split on a pattern

import re

# ── 10.1 re.search() — find the FIRST match ───────
# Returns a Match object (truthy) or None (falsy).
text = "Sourav is a good boy, sourav eats an egg regularly"

m = re.search("sourav", text)     # case-sensitive by default
print(m)                           # <re.Match object: span=(22, 28), match='sourav'>

if m:
    print("Match found!")
    print("Matched text :", m.group())        # sourav
    print("Start index  :", m.start())        # 22
    print("End index    :", m.end())          # 28
    print("Span         :", m.span())         # (22, 28)
else:
    print("No match found.")

# ── 10.2 re.search() with re.IGNORECASE flag ──────
# re.IGNORECASE (or re.I) makes matching case-insensitive.
m2 = re.search("sourav", text, re.IGNORECASE)
if m2:
    print("\nWith IGNORECASE — matched:", m2.group())    # Sourav (the FIRST one)
    print("Start:", m2.start())                          # 0

# ── 10.3 re.findall() — find ALL matches ──────────
# Returns a plain list of matching strings (no Match objects).
all_matches = re.findall("sourav", text, re.IGNORECASE)
print("\nAll matches:", all_matches)    # ['Sourav', 'sourav']
print("Count:", len(all_matches))      # 2

# ── 10.4 re.sub() — search AND replace ───────────
# Like str.replace() but uses a pattern instead of fixed text.
new_text = re.sub("good", "bad", text)
print("\nAfter sub:", new_text)        # "... a bad boy ..."

# Replace only the FIRST N occurrences with count= parameter
new_text2 = re.sub("sourav", "OYAJ", text, count=1, flags=re.IGNORECASE)
print("First only:", new_text2)        # replaces only first "Sourav"

# Replace eats with "doesn't eat"
new_text3 = re.sub("eats", "doesn't eat", text)
print("Sub:", new_text3)

# ── 10.5 re.match() — match at the START only ─────
# re.match() only checks the BEGINNING of the string.
# Use re.search() if the match can be anywhere.
m3 = re.match("Sourav", text)          # starts with "Sourav"? YES
print("\nre.match at start:", m3.group() if m3 else "No match")

m4 = re.match("sourav", text)          # lowercase at start? NO
print("re.match lowercase:", m4)       # None

# ── 10.6 re.split() — split on a pattern ──────────
csv = "apple, banana,   mango  ,lichi"
parts = re.split(r",\s*", csv)         # split on comma + any spaces
print("\nSplit result:", parts)        # ['apple', 'banana', 'mango', 'lichi']

# ── 10.7 Pattern Basics ───────────────────────────
# Regular expressions are patterns, not just fixed strings.
# Here are the most important pattern symbols:
#
#  SYMBOL   MEANING                          EXAMPLE MATCH
#  ──────────────────────────────────────────────────────────
#  .        any single character (except \n)  "a", "9", "@"
#  \d       any digit [0-9]                  "3", "7"
#  \w       word character [a-zA-Z0-9_]      "a", "Z", "_"
#  \s       whitespace (space, tab, newline)  " ", "\t"
#  \D       NOT a digit                       "a", "!"
#  \W       NOT a word character              " ", "!"
#  \S       NOT whitespace                    "a", "3"
#  ^        start of string                   "^Hello"
#  $        end of string                     "world$"
#  *        0 or more of preceding            "go*" → "g","go","gooo"
#  +        1 or more of preceding            "go+" → "go","gooo"
#  ?        0 or 1 of preceding (optional)    "colou?r" → "color","colour"
#  {n}      exactly n repetitions             "\d{4}" → "2025"
#  {n,m}    between n and m repetitions       "\d{2,4}"
#  [abc]    any one of a, b, c               "[aeiou]"
#  [^abc]   any character EXCEPT a, b, c     "[^0-9]"
#  (abc)    group — capture this part        "(hello)+"
#  |        OR                               "cat|dog"

# ── 10.8 Practical pattern examples ───────────────

# Find all numbers in a string
sentence = "I have 3 cats and 12 dogs and 100 fish."
nums = re.findall(r"\d+", sentence)      # \d+ = one or more digits
print("\nNumbers found:", nums)          # ['3', '12', '100']

# Validate an email (simplified pattern)
emails = ["sourav@gmail.com", "bad-email", "test@cs.edu", "no_at_sign"]
pattern = r"\w+@\w+\.\w+"               # word@word.word
for email in emails:
    if re.search(pattern, email):
        print(f"✅ Valid email:   {email}")
    else:
        print(f"❌ Invalid email: {email}")

# Extract all words starting with a capital letter
bio = "Sourav studies Computer Science in Dhaka University."
caps = re.findall(r"\b[A-Z][a-z]+", bio)
print("\nCapitalized words:", caps)     # ['Sourav', 'Computer', 'Science', 'Dhaka', 'University']

# Find all words with exactly 4 letters
words4 = re.findall(r"\b\w{4}\b", sentence)
print("4-letter words:", words4)

# Replace ALL whitespace (spaces, tabs) with a single space
messy = "hello    world\there    we   go"
clean = re.sub(r"\s+", " ", messy).strip()
print("Cleaned:", clean)               # "hello world here we go"

# ── 10.9 Flags summary ────────────────────────────
#  FLAG              SHORTHAND   MEANING
#  ────────────────────────────────────────────────
#  re.IGNORECASE     re.I        case-insensitive matching
#  re.MULTILINE      re.M        ^ and $ match each LINE (not whole string)
#  re.DOTALL         re.S        "." also matches newline \n
#  re.VERBOSE        re.X        allow comments and whitespace in pattern

# Multiple flags: combine with | (pipe)
m_flags = re.search("SOURAV", text, re.IGNORECASE | re.MULTILINE)
print("\nMulti-flag match:", m_flags.group() if m_flags else "None")

# ── 10.10 re vs str methods — when to use each ────
#
#  str method    Use when...
#  ───────────────────────────────────────────────────────────
#  in            simple substring check: "hello" in text
#  str.find()    fixed string, get position of first match
#  str.replace() fixed string, replace all occurrences
#  str.split()   split on a fixed delimiter
#
#  re function   Use when...
#  ───────────────────────────────────────────────────────────
#  re.search()   pattern anywhere, get position and groups
#  re.findall()  extract ALL occurrences of a pattern
#  re.sub()      replace pattern (with captured groups, counts)
#  re.split()    split on variable whitespace or complex delimiters

# ✅ TASK 1: Use re.findall() to extract all email addresses from:
#            "Contact us at help@test.com or support@site.org for info."
# ✅ TASK 2: Use re.sub() to REMOVE all digits from "abc123def456ghi789".
#            (Replace r"\d+" with "")
# ✅ TASK 3: Use re.split() to split "one1two2three3four" on any digit.
# ✅ TASK 4: Write a function is_valid_phone(s) that returns True if s
#            matches the pattern: 3 digits, dash, 7 digits  (e.g. "017-1234567").
# ✅ TASK 5: Extract all words between 5 and 8 letters long from any sentence.


# %%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SECTION 11 — FINAL CLEANUP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Remove all demo files created during this session.

import os, shutil

files_to_remove = [
    "msg.txt", "sourav.txt", "fruits.txt",
    "notes.txt", "msg_copy.txt", "unique.txt",
    "output.txt", "poem.txt", "fruits_backup.txt",
    "archived_notes.txt", "msg_backup.txt",
    "sourav_backup.txt", "info.txt",
]
for f in files_to_remove:
    if os.path.exists(f):
        os.remove(f)
        print(f"  Removed: {f}")

for folder in ["parent", "parent_backup", "subfolder", "backups", "test_folder"]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"  Removed folder: {folder}/")

print("\n✅ All demo files cleaned up.")


# ============================================================
#  END OF FILE 6 — PYTHON MODULES & STANDARD LIBRARY
#
#  Summary of what you learned:
#    1.  File modes         — "r", "w", "a", "x", "b"
#    2.  Writing files      — write(), writelines(), "w" vs "a"
#    3.  Reading files      — read(), readline(), readlines(), loop
#    4.  Appending          — "a" mode, adding content safely
#    5.  with statement     — context manager, auto-close
#    6.  File error handling — FileNotFoundError, PermissionError
#    7.  os module          — getcwd, listdir, path checks, mkdir, remove
#    8.  shutil module      — copy, copy2, copytree, move, rmtree
#    9.  argparse           — CLI arguments, positional vs optional
#   10.  re module          — search, findall, sub, match, split, patterns
#
#  Next: explore datetime, csv, sqlite3, and requests modules!
# ============================================================
