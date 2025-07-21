# 🐍 Python Day 4: Loops + Lists

## 📚 Overview

This lesson covers Python's loop structures and lists. It includes basic usage of `for` and `while` loops, the `range()` function, list operations like `.append()` and `.sort()`, and ends with a mini project — a number guessing game.

---

## 🔁 1. Loops in Python

### ✅ `for` loop

Used to repeat a block of code a specific number of times.

```python
for i in range(5):
    print(i)
```

* `range(5)` → returns numbers: 0, 1, 2, 3, 4

### ✅ `while` loop

Repeats as long as a condition is `True`.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

* Make sure to update the variable to avoid infinite loops.

---

## 🔢 2. `range()` Function

```python
range(stop)              → 0 to stop-1
range(start, stop)       → start to stop-1
range(start, stop, step) → start to stop-1 with step size
```

### Examples:

```python
range(3)        # 0, 1, 2
range(1, 4)     # 1, 2, 3
range(0, 10, 2) # 0, 2, 4, 6, 8
```

---

## 📃 3. Python Lists

Lists store multiple values in a single variable.

```python
colors = ["red", "green", "blue"]
```

### ✅ Accessing Items

```python
colors[0]    # "red"
colors[-1]   # "blue"
```

### ✅ List Methods

```python
colors.append("yellow")  # Add item to end
colors.sort()            # Sort items
len(colors)              # Get list length
```

---

## 🔄 4. Looping Through a List

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

---

## 🎮 Mini Project: Number Guessing Game

```python
import random

number = random.randint(1, 10)
attempts = 0

print("Guess the number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
```

---

## 🧐 Summary Table

| Concept      | Example               | Description                             |
| ------------ | --------------------- | --------------------------------------- |
| `for` loop   | `for i in range(5):`  | Repeat fixed number of times            |
| `while` loop | `while x < 5:`        | Repeat while condition is true          |
| `range()`    | `range(1, 6)`         | Generate sequence of numbers            |
| `.append()`  | `list.append("item")` | Add item to list                        |
| `.sort()`    | `list.sort()`         | Sort list alphabetically or numerically |
| Indexing     | `list[0]`, `list[-1]` | Access items from list                  |

---

## ✅ What's Next?

You’re now ready to move on to **Day 5: Functions and Modules**. Stay consistent and keep building!
