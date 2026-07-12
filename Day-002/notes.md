# 📘 Python Data Types - Numbers (int & float)

## 🎯 Learning Objective

In this lesson, we learned how to use Python's numeric data types (`int` and `float`) to build simple real-world applications.

---

# What are Data Types?

A data type tells Python what kind of value a variable stores.

```python
age = 20          # int
price = 99.99     # float
name = "Arindom"  # str
is_student = True # bool
```

---

# Integer (int)

An integer is a whole number.

Examples:

```python
age = 21
marks = 95
temperature = -5
```

Characteristics:

- No decimal point
- Positive or negative
- Unlimited size in Python

---

# Float (float)

A float is a number containing a decimal point.

Examples:

```python
height = 5.8
price = 999.99
pi = 3.14159
```

Characteristics:

- Contains decimals
- Used for precise calculations

---

# Getting User Input

The `input()` function always returns a string.

Example:

```python
age = input("Enter your age: ")
```

Output:

```
21
```

The value stored is:

```python
"21"
```

---

# Type Conversion

Convert input into the required data type.

### Integer

```python
age = int(input("Enter age: "))
```

### Float

```python
salary = float(input("Enter salary: "))
```

---

# Arithmetic Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 5 + 2 |
| - | Subtraction | 5 - 2 |
| * | Multiplication | 5 * 2 |
| / | Division | 5 / 2 |
| // | Floor Division | 5 // 2 |
| % | Modulus | 5 % 2 |
| ** | Exponent | 5 ** 2 |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# Using round()

The `round()` function limits decimal places.

Example:

```python
value = 8333.333333

print(round(value, 2))
```

Output:

```
8333.33
```

---

# Project 1: EMI Calculator

## Formula

```
EMI = Loan Amount / Number of Months
```

Example:

```
Loan Amount = 500000

Months = 60

EMI = 8333.33
```

Concepts Used:

- float()
- int()
- Variables
- Division
- round()

---

# Project 2: Shopping Bill Calculator

## Steps

1. Take prices of three items.
2. Calculate subtotal.
3. Add GST (18%).
4. Apply 10% discount if subtotal > 5000.
5. Calculate final bill.

Formula:

```
Subtotal = Item1 + Item2 + Item3

GST = Subtotal × 18%

Discount = 10% of subtotal (only if subtotal > 5000)

Final Bill = Subtotal + GST - Discount
```

Concepts Used:

- float()
- Addition
- Multiplication
- if-else
- Variables

---

# Project 3: Tip Calculator

Formula:

```
Tip Amount = Bill × Tip Percentage ÷ 100

Total Bill = Bill + Tip Amount
```

Example:

```
Bill = 2400

Tip = 10%

Tip Amount = 240

Total = 2640
```

Concepts Used:

- float()
- Percentage calculation
- Arithmetic operators

---

# Percentage Formula

General formula:

```
Percentage = (Value × Percentage) / 100
```

Example:

```python
discount = subtotal * 10 / 100
```

or

```python
discount = subtotal * 0.10
```

Both give the same result.

---

# Order of Operations (PEMDAS)

Python follows this order:

1. Parentheses `()`
2. Exponents `**`
3. Multiplication `*`
4. Division `/`
5. Floor Division `//`
6. Modulus `%`
7. Addition `+`
8. Subtraction `-`

Example:

```python
answer = 5 + 2 * 3
```

Output:

```
11
```

Because multiplication happens first.

---

# Common Beginner Mistakes

### ❌ Forgetting type conversion

```python
age = input("Age: ")
```

Correct:

```python
age = int(input("Age: "))
```

---

### ❌ Using `=` instead of `==`

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

### ❌ Forgetting parentheses

Wrong:

```python
print
```

Correct:

```python
print()
```

---

### ❌ Dividing by zero

Wrong:

```python
10 / 0
```

Always ensure the denominator is not zero.

---

# Key Functions Learned

```python
input()
print()
int()
float()
round()
```

---

# Key Concepts Learned

- Data Types
- int
- float
- Variables
- User Input
- Type Conversion
- Arithmetic Operators
- Percentage Calculations
- Conditional Statements (`if`, `else`)
- Real-World Calculations

---

# Mini Exercises

### Exercise 1

Create a BMI Calculator.

Formula:

```
BMI = Weight / Height²
```

---

### Exercise 2

Create a Temperature Converter.

```
Celsius → Fahrenheit

F = C × 9/5 + 32
```

---

### Exercise 3

Create a Student Marks Calculator.

Calculate:

- Total
- Average
- Percentage

---

### Exercise 4

Create an Area Calculator.

Calculate area of:

- Circle
- Rectangle
- Square
- Triangle

---

# Summary

After this lesson, you should be able to:

✅ Store numbers using `int` and `float`

✅ Accept numeric input from users

✅ Perform arithmetic calculations

✅ Convert strings into numbers

✅ Use `round()` for cleaner output

✅ Build simple real-world Python applications

- EMI Calculator
- Shopping Bill Calculator
- Tip Calculator

These concepts form the foundation for almost every Python program you will write.
