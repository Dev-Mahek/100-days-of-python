# Conditional Statements in Python 🐍

## What are Conditional Statements?

Conditional statements allow a program to **make decisions** based on whether a condition is `True` or `False`.

### Real-Life Examples
- If it is raining → Take an umbrella.
- If you have enough money → Buy coffee.
- If your score is above 90 → Grade A.

---

# 1. The `if` Statement

The `if` statement executes a block of code **only when the condition is True**.

### Syntax

```python
if condition:
    # Code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("You can vote.")
```

### Output

```
You can vote.
```

### Explanation

Python checks:

```python
age >= 18
```

Since `20 >= 18` is `True`, Python executes the indented code.

---

# 2. Comparison Operators

Comparison operators are used inside conditions.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not Equal | `age != 18` |
| `>` | Greater Than | `age > 18` |
| `<` | Less Than | `age < 18` |
| `>=` | Greater Than or Equal To | `age >= 18` |
| `<=` | Less Than or Equal To | `age <= 18` |

### Example

```python
marks = 80

if marks >= 40:
    print("Passed")
```

---

# 3. The `if...else` Statement

Use `else` when you want another block of code to run if the condition is `False`.

### Syntax

```python
if condition:
    # True block
else:
    # False block
```

### Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Output

```
Minor
```

---

# 4. The `if...elif...else` Statement

Use `elif` when there are **multiple conditions**.

### Example

```python
marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

### Output

```
Grade C
```

> Python checks conditions from top to bottom and stops at the first condition that is `True`.

---

# 5. Nested `if`

An `if` statement can be placed inside another `if`.

### Example

```python
age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
```

### Output

```
You can drive.
```

---

# 6. Logical Operators

## `and`

Both conditions must be `True`.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

---

## `or`

At least one condition must be `True`.

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

## `not`

Reverses the Boolean value.

```python
logged_in = False

if not logged_in:
    print("Please log in.")
```

---

# Mini Project: Restaurant Bill Discount Calculator

## Problem Statement

Create a program that:

- Takes the bill amount from the user.
- Gives a **20% discount** for bills of ₹5000 or more.
- Gives a **10% discount** for bills of ₹2000 or more.
- Gives **no discount** otherwise.
- Displays:
  - Original Bill
  - Discount
  - Final Bill

---

## Step 1: Get User Input

```python
bill = float(input("Enter your bill amount: ₹"))
```

### Explanation

- `input()` reads data from the keyboard.
- It always returns a **string**.
- `float()` converts the input into a decimal number so we can perform calculations.

Example:

```
User enters: 3500
```

Stored as:

```python
3500.0
```

---

## Step 2: Calculate the Discount

```python
if bill >= 5000:
    discount = bill * 0.20
elif bill >= 2000:
    discount = bill * 0.10
else:
    discount = 0
```

### How It Works

If:

```python
bill = 6500
```

Then:

```
6500 × 20% = 1300
```

So:

```python
discount = 1300
```

If:

```python
bill = 3000
```

Then:

```
3000 × 10% = 300
```

If:

```python
bill = 1500
```

Then:

```
Discount = 0
```

---

## Step 3: Calculate Final Bill

```python
final_bill = bill - discount
```

Example:

```
Original Bill = ₹3500
Discount = ₹350

Final Bill = ₹3150
```

---

## Step 4: Display the Receipt

```python
print("\n----- BILL SUMMARY -----")
print(f"Original Bill : ₹{bill:.2f}")
print(f"Discount      : ₹{discount:.2f}")
print(f"Final Bill    : ₹{final_bill:.2f}")
```

### Why Use an f-string?

An f-string allows variables to be inserted directly into a string.

Example:

```python
name = "Arindom"

print(f"Hello, {name}")
```

Output:

```
Hello, Arindom
```

---

### What Does `:.2f` Mean?

It formats a number to **2 decimal places**.

Example:

```python
3500
```

becomes:

```
3500.00
```

---

# Complete Program

```python
# Restaurant Bill Discount Calculator

bill = float(input("Enter your bill amount: ₹"))

if bill >= 5000:
    discount = bill * 0.20
elif bill >= 2000:
    discount = bill * 0.10
else:
    discount = 0

final_bill = bill - discount

print("\n----- BILL SUMMARY -----")
print(f"Original Bill : ₹{bill:.2f}")
print(f"Discount      : ₹{discount:.2f}")
print(f"Final Bill    : ₹{final_bill:.2f}")
```

---

# Sample Output

```
Enter your bill amount: ₹3500

----- BILL SUMMARY -----
Original Bill : ₹3500.00
Discount      : ₹350.00
Final Bill    : ₹3150.00
```

---

# Key Takeaways

- Use `if` to execute code when a condition is `True`.
- Use `else` for the alternative path.
- Use `elif` to check multiple conditions.
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) return `True` or `False`.
- Logical operators:
  - `and` → All conditions must be `True`.
  - `or` → At least one condition must be `True`.
  - `not` → Reverses a Boolean value.
- `input()` returns a string.
- Use `int()` or `float()` to convert user input into numbers.
- Use **f-strings** to format output.
- `:.2f` displays numbers with **2 decimal places**.

---

# Practice Exercises

1. Check if a person is eligible to vote.
2. Create a login system using a password.
3. Display grades based on marks.
4. Build an ATM PIN checker.
5. Extend the Restaurant Bill Calculator by adding:
   - Customer name
   - Membership discount
   - Receipt with total savings
