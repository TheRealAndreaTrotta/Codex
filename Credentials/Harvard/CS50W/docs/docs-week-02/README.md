# Python from Scratch

> For anyone who’s **never written a line of Python**. We’ll start from the core idea (why Python), then move to installation, syntax, and foundational concepts. Every section comes with working examples. By the end you’ll know how to run scripts, organize code into modules, use OOP and FP, and handle exceptions.

---

## Table of Contents

0. [Introduction](#introduction)
1. [Variables](#variables)
2. [Formatting Strings](#formatting-strings)
3. [Conditions](#conditions)
4. [Sequences](#sequences)
5. [Strings](#strings)
6. [Lists](#lists)
7. [Tuples](#tuples)
8. [Sets](#sets)
9. [Dictionaries](#dictionaries)
10. [Loops](#loops)
11. [Functions](#functions)
12. [Modules](#modules)
13. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
14. [Functional Programming (FP)](#functional-programming-fp)
15. [Decorators](#decorators)
16. [Lambda Functions](#lambda-functions)
17. [Exceptions](#exceptions)
18. [REPL vs Script, Interpreter, and pip](#repl-vs-script-interpreter-and-pip)

---

## Introduction

So far (in the web track) we’ve seen **HTML and CSS** to build pages and **Git/GitHub** to version code and collaborate. Today we dive into **Python**, one of the two main languages we’ll use in the course.

> We’ll use **Python 3**. **Python 2** still exists in legacy projects, but when you search online **make sure** the material targets Python 3.

**Why Python?**

* Powerful and widely used: lets you quickly build even complex web apps.
* Huge ecosystem of libraries.
* Clean syntax → great for beginners, still solid for pros.

**Hello, world**

```python
print("Hello, world!")
```

Here we use the built-in `print` function, which takes an argument in parentheses and **shows it in the terminal**.

**How to run it on your machine**

1. Write that line in an editor and save as `example.py`.
2. Open the terminal, `cd` to the file’s folder.
3. Run:

```bash
python3 example.py   # on many systems it’s python3
```

If your system uses `python` instead of `python3`, use that. If Python isn’t installed, **install it** (and install **pip** too—we’ll use it later).

**Interpreter vs compilation**
When you run `python file.py`, the **interpreter** reads the file **line by line** and executes it. That’s different from languages like C or Java, which **compile** to machine code first.

---

## Variables

Assign with `=`:

```python
a = 28
b = 1.5
c = "Hello!"
d = True
e = None
```

Python **infers types** (you don’t have to declare them). Common types:

* `int`: integer
* `float`: decimal
* `str`: string (sequence of characters)
* `bool`: `True`/`False`
* `NoneType`: special value `None` (absence of a value)

**User input**

```python
name = input("Name: ")
print("Hello, " + name)
```

On the first line, `name` receives **whatever `input` returns**. On the second, we use `+` to **concatenate** strings (in Python `+` adds numbers and concatenates strings/lists).

---

## Formatting Strings

**f-strings** make this much simpler:

```python
name = "Andrea"
print(f"Hello, {name}")
# you can embed functions/expressions too
print(f"2 + 2 = {2 + 2}")

# one-liner equivalent of the example above
print(f"Hello, {input('Name: ')}")
```

---

## Conditions

```python
num = int(input("Number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
```

A **conditional** contains `if`/`elif`/`else` and (except for `else`) a **boolean expression** that evaluates to `True` or `False`.
**Indentation** is **required** in Python (usually 4 spaces) and defines what belongs to each block.

> ⚠️ `input()` always returns a **string** → if you need to compare with numbers, **cast** with `int(...)`. Without casting you’ll get a `TypeError` (you were comparing `str` with `int`).

---

## Sequences

A major strength of Python is working with **sequences** of data.

### Strings

**Ordered:** Yes · **Mutable:** No

```python
name = "Harry"
print(name[0])  # 'H'
print(name[1])  # 'a'
```

### Lists

**Ordered:** Yes · **Mutable:** Yes

```python
names = ["Harry", "Ron", "Hermione"]
print(names)        # whole list
print(names[1])     # second element
names.append("Draco")
names.sort()
print(names)
```

### Tuples

**Ordered:** Yes · **Mutable:** No

```python
point = (12.5, 10.6)
```

### Sets

**Ordered:** No · **Mutable:** (special) — no duplicates

```python
s = set()
s.add(1); s.add(2); s.add(3); s.add(4)
s.add(3); s.add(1)     # duplicates ignored
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")
# Possible output: {1, 3, 4}\nThe set has 3 elements.
```

### Dictionaries

**Ordered:** No (CPython 3.7+ preserves insertion order) · **Mutable:** Yes

```python
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])           # Gryffindor
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])        # Gryffindor
```

---

## Loops

Two main forms: `for` and `while`. Let’s start with `for`.

```python
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
```

Same result with `range`:

```python
for i in range(6):
    print(i)  # 0..5
```

Iterating a list of names:

```python
names = ["Harry", "Ron", "Hermione"]
for name in names:
    print(name)
```

Iterating the characters of a string:

```python
name = "Harry"
for ch in name:
    print(ch)
```

---

## Functions

Define and reuse behavior:

```python
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

---

## Modules

As projects grow, split functions across files.

`functions.py`:

```python
def square(x):
    return x * x
```

`square.py`:

```python
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

Alternatively, import the whole module and use **dot notation**:

```python
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
```

Remember there are **built-in modules** (e.g., `math`, `csv`) and you can install more with **pip** (e.g., `Django`, which we’ll use for the web later).

---

## Object-Oriented Programming (OOP)

OOP organizes code around **objects** that **store data** and **expose methods**.

**Simple `Point` class**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)
```

**More realistic example: `Flight`**

```python
class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
```

> Note: In Python, `0` is “falsy” → `if not self.open_seats():` is `True` when there are no seats left.

---

## Functional Programming (FP)

Python also supports a **functional** style: functions are values and can be passed/returned.

### Decorators

A **decorator** is a function that modifies another function’s behavior.

```python
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()
```

### Lambda Functions

**Lambdas** create anonymous functions; handy when you need one briefly.

```python
square = lambda x: x * x
```

Practical example: sort a list of dictionaries by name.

```python
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])  # sort by name
print(people)
```

---

## Exceptions

Runtime errors raise **exceptions**. We can **handle** them with `try`/`except`.

Simple division:

```python
x = int(input("x: "))
y = int(input("y: "))

result = x / y
print(f"{x} / {y} = {result}")
```

If `y` is `0` → `ZeroDivisionError`. Let’s handle it:

```python
import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
```

If the user enters non-numeric text → `ValueError`. Handle both:

```python
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
```

---

## REPL vs Script, Interpreter, and pip

* **REPL**: start it with `python3` (type `exit()` or press `Ctrl+D` to quit).
* **Script**: save code to `file.py` and run `python3 file.py`.
* **Interpreter**: Python reads and executes line by line (doesn’t compile like C/Java).
* **pip**: package manager. Examples:

```bash
python3 -m pip --version
python3 -m pip install requests
python3 -m pip install django
```

> On some systems you might use `pip3`/`python` instead of `python3`.

---

### Ready for the next lesson

Next time we’ll switch to **Django** (web framework) and connect what you’ve learned to a real web application.

---

## Deep Dives — CS50 mix + “pro” practice

### REPL vs Script vs Notebook

* **REPL** (`python3`): perfect to try one line at a time.
* **Script** (`python3 file.py`): for real programs, versioned with Git.
* **Notebook** (Jupyter): great for data/AI, but for web/CLI keep `.py` files.

### Types, identity, and mutability

* **Equality** `==` vs **Identity** `is` (same object in memory).
* Mutable: `list`, `dict`, `set`. Immutable: `tuple`, `str`, `int`, `float`, `frozenset`.
* Copies: `a = b` is aliasing. Use `list(a)` / `a.copy()` for **shallow copy**, `copy.deepcopy(a)` for **deep copy**.

### Slicing and unpacking

```python
nums = [0,1,2,3,4,5]
print(nums[1:4])   # [1,2,3]
head, *body, tail = nums  # advanced unpacking
```

### Comprehensions & generators

```python
squares = [n*n for n in range(10)]                 # list comp
unique_evens = {n for n in range(20) if n%2==0}    # set comp
index_map = {i: ch for i, ch in enumerate('kai')}  # dict comp

# generator expression (lazy)
odd = (n for n in range(1000000) if n%2)

# generator with yield
def count_up_to(n):
    c = 1
    while c <= n:
        yield c
        c += 1
```

### Context managers (`with`)

```python
# safe file I/O
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello from Python!\n")
# the file is closed automatically
```

### File I/O & JSON with `pathlib`

```python
from pathlib import Path
import json

path = Path("data.json")
data = {"ok": True, "items": [1,2,3]}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["items"])  # [1,2,3]
```

### Type hints (PEP 484) & dataclass

```python
from typing import Optional, Iterable
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: Optional[int] = None

def avg(xs: Iterable[float]) -> float:
    total = 0.0
    count = 0
    for x in xs:
        total += x
        count += 1
    return total / count if count else 0.0
```

Run a **type-check** with `mypy` (optional): `python3 -m pip install mypy` → `mypy file.py`.

### `__name__ == "__main__"` and CLI with `argparse`

```python
import argparse

def main():
    p = argparse.ArgumentParser(description="Demo CLI")
    p.add_argument("name")
    p.add_argument("--times", type=int, default=1)
    args = p.parse_args()
    for _ in range(args.times):
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
```

Example: `python3 app.py Andrea --times 3`.

### Virtual environments & dependencies

```bash
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
python -m pip install --upgrade pip
pip install requests
pip freeze > requirements.txt
# restore
pip install -r requirements.txt
```

Suggested: **pipx** (for global tools), **uv/poetry** (advanced project management).

### Quick testing (pytest)

`calc.py`

```python
def add(a, b):
    return a + b
```

`test_calc.py`

```python
from calc import add

def test_add():
    assert add(2, 3) == 5
```

```bash
python -m pip install pytest
pytest -q
```

### Debugging & logging

```python
# interactive breakpoint
x = 42
breakpoint()  # enters pdb since Python 3.7+

# basic logging
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Starting…")
```

### Style (PEP 8) & tooling

* Names: `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_CASE` for constants.
* **black** (format), **ruff/flake8** (lint), **isort** (imports).
* Docstrings `"""Explain what it does, parameters and returns"""`.

### Advanced OOP

```python
class Account:
    bank = "KaiBank"          # class attribute
    def __init__(self, owner, balance=0.0):
        self.owner = owner     # instance attribute
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("amount must be > 0")
        self._balance += amount

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self._balance:.2f})"
```

Or with **dataclasses**:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

### Practical FP

```python
from functools import lru_cache, partial

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

pow10 = partial(pow, 10)  # pow10(x) == pow(10, x)
```

### Advanced exceptions

```python
class NotEnoughFunds(Exception):
    pass

try:
    raise NotEnoughFunds("Balance too low")
except NotEnoughFunds as e:
    print("Transfer failed:", e)
else:
    print("Ok")
finally:
    print("Always executed")
```

---

## Mini-project: To-Do CLI (JSON file)

**Requirements**

* Commands: `add`, `list`, `done` (complete & remove).
* Persist data in `todo.json`.
* Solid against missing/bad inputs.

`todo.py`

```python
from __future__ import annotations
import argparse, json
from pathlib import Path

DB = Path("todo.json")

def load():
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8"))
    return {"tasks": []}

def save(data):
    DB.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def cmd_add(text: str):
    data = load()
    data["tasks"].append({"text": text, "done": False})
    save(data)
    print("Added:", text)

def cmd_list():
    data = load()
    if not data["tasks"]:
        print("(no tasks)")
        return
    for i, t in enumerate(data["tasks"], 1):
        mark = "✓" if t["done"] else "✗"
        print(f"{i:2}. [{mark}] {t['text']}")

def cmd_done(index: int):
    data = load()
    i = index - 1
    if i < 0 or i >= len(data["tasks"]):
        raise IndexError("Task index out of range")
    data["tasks"][i]["done"] = True
    save(data)
    print("Completed:", data["tasks"][i]["text"])

def main():
    p = argparse.ArgumentParser(prog="todo", description="Simple To-Do CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add")
    p_add.add_argument("text")

    sub.add_parser("list")

    p_done = sub.add_parser("done")
    p_done.add_argument("index", type=int)

    args = p.parse_args()

    if args.cmd == "add":
        cmd_add(args.text)
    elif args.cmd == "list":
        cmd_list()
    elif args.cmd == "done":
        cmd_done(args.index)

if __name__ == "__main__":
    main()
```

**Usage**

```bash
python3 todo.py add "Study Python"
python3 todo.py list
python3 todo.py done 1
```

---

## Exercises (recommended)

* Write `is_even(n)` and test it with `assert`.
* With a **list comprehension**, create multiples of 3 below 100.
* Given `people = [{"name":"A","age":20}, …]`, sort by age (lambda).
* Implement a **custom context manager** that times a block (`time.perf_counter`).
* Add a `clear` command with confirmation to the To-Do CLI.
* Add **type hints** everywhere and run `mypy`.
* Write `pytest` tests for `cmd_add`/`cmd_done` using a temporary DB file.
* Refactor `Flight` to use a `dataclass` `Passenger(name: str)`.

---

## Conceptual Guide — utility, potential & trade-offs (not just code)

> Here’s **why** you’ll use each concept, **when** it helps, and **what to avoid**. Fewer examples, more strategy.

### Interpreter vs compilation

**Why it matters:** Python’s interpreter runs line by line → great for **prototyping** and **automation**. Compiled languages (C/Java) deliver max performance but slower dev cycles.
**Trade-off:** Python is slower on pure CPU-bound tasks, but you often win with C-optimized libs (NumPy) and **productivity**.

### REPL vs Script vs Notebook

* **REPL**: quick experiments, verify functions, fast debugging.
* **Script**: automation, CLIs, scheduled jobs, versioned projects.
* **Notebook**: data analysis, AI/ML, exploratory reports.
  **Avoid:** notebooks for production logic; promote to testable `.py` modules.

### Variables and types (dynamic)

**Why:** dynamic typing speeds development and reduces boilerplate.
**Caveat:** type errors appear **at runtime**; use **type hints** + `mypy` to prevent bugs.
**Key ideas:** `None` as “no value”; “truthiness” (0, '', [], {}, None are falsy).

### Strings & f-strings

**Why:** readable, safe formatting (avoid fragile concatenation).
**When:** logs, user messages, reporting.
**Avoid:** using unvalidated inputs in f-strings in sensitive contexts (sanitize).

### Conditions

**Why:** separate key cases.
**Patterns:** **guard clauses** (return early on invalids), `match` for multi-way branching.
**Avoid:** deep nested `if`s; prefer small functions and explicit names.

### Sequences: pick the right structure

* **list**: ordered, mutable, general purpose.
* **tuple**: immutable, lightweight records (coordinates, keys).
* **set**: membership/duplicates; fast set ops.
* **dict**: key→value mapping, backbone of many app structures.
  **Average complexity:** `in` on set/dict ≈ O(1), on list/tuple ≈ O(n).

### Loops & iteration

**Why:** traverse collections.
**Patterns:** `enumerate` for indices, `zip` to advance in parallel, generators for infinite or huge streams.
**Avoid:** mutating a list while iterating it (use a copy or comprehensions).

### Functions

**Why:** reuse, testability, composition.
**Best practices:** one function = one responsibility; docstrings; keyword args.
**Trap:** **mutable defaults**. Don’t do `def f(x=[])`; use `None` and create inside: `x = [] if x is None else x`.

### Modules & packages

**Why:** organize code, clear **namespaces**, reuse.
**Concepts:** absolute imports, packages with `__init__.py`, entry-point via `if __name__ == "__main__"`.
**Avoid:** circular imports (refactor into shared modules).

### OOP (objects, not just classes)

**Why:** model entities with **data + behavior**; enforce invariants (e.g., `balance >= 0`).
**Guidelines:** prefer **composition** over inheritance; use `@property` for validation; `__repr__` helps debugging.
**Dataclasses:** convenient for data-objects (less boilerplate) → note: mutable by default.

### Practical FP

**Why:** declarative transformations, less shared state.
**Tools:** `map`/`filter`, **lambda** for quick callbacks, `functools` (`lru_cache`, `partial`).
**Avoid:** opaque lambda chains; if readability drops, write named functions.

### Comprehensions & generators

**Why:** **expressive** collection building; generators are **lazy** and save memory.
**When:** large datasets/streams → generators; small lists → list comp.
**Tools:** `itertools` (`chain`, `groupby`, `islice`).

### Context managers

**Why:** **safe** resource management (files, locks, connections).
**How:** `with` guarantees cleanup on exceptions.
**Custom:** implement `__enter__/__exit__` or use `contextlib.contextmanager`.

### Type hints

**Why:** smarter IDEs, safer refactors, explicit contracts.
**Note:** not enforced at runtime; use `mypy/pyright` to check them.
**Advanced:** `Protocol`, `TypedDict`, `Literal` for more precise models.

### Exceptions

**Why:** error flow **separate** from normal flow.
**Patterns:** `try/except/else/finally`, **domain** exceptions.
**Avoid:** catching `Exception` in huge blocks; keep scope tight and log context.

### Virtual environments & dependencies

**Why:** **isolation** and reproducibility.
**Patterns:** `requirements.txt` for quick pins; `pyproject.toml` (poetry/uv) for modern projects.
**Avoid:** sharing global dependencies across projects.

### Testing (pytest)

**Why:** confidence in refactors, prevent regressions.
**Techniques:** `parametrize`, **fixtures** for clean setup, `coverage` to measure.

### Debugging & logging

**Why:** observability.
**Tools:** `breakpoint()` to inspect state; log levels (`DEBUG`→`CRITICAL`).
**Avoid:** leftover `print` debugging in production code.

### Style (PEP 8) & tooling

**Why:** team readability.
**Suggested stack:** **black** (format), **ruff** (lint), **isort** (imports), **pre-commit** (hooks).
**CI:** integrate test+lint in workflows (GitHub Actions).

### CLI with `argparse`

**Why:** turn scripts into **tools** with help and parameters.
**UX:** clear descriptions, exit codes (`sys.exit`), helpful messages.

### Performance: when to think about it

**First:** pick the right data structure.
**Measure:** `timeit`, profilers (`cProfile`).
**Optimize:** use C-optimized built-ins, avoid premature micro-optimizations.

### Data & formats

**JSON:** web-friendly; **CSV:** tabular; **YAML/TOML:** config.
**Schema:** dataclasses/`pydantic` for validation (when needed).

---

## Course Mental Map (keep this in mind)

1. **Core:** syntax, types, sequences, functions.
2. **Structure:** modules, packages, OOP/FP.
3. **Robustness:** exceptions, type hints, tests, logging.
4. **Product:** CLI, environments, packaging, performance.
5. **Next steps:** **Django/FastAPI** (web), **pandas/NumPy** (data), **automation** (scheduled scripts).