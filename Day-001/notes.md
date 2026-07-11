# 📝 Python Notes – Day 1: Variables & User Input

## 📌 What is a Variable?

A **variable** is a named container used to store data in memory.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Arindom"
age = 24
height = 5.9
is_student = True
```

---

## 📌 Variable Naming Rules

✅ Valid Variable Names

```python
name = "John"
my_age = 24
student1 = "Alice"
_total = 100
```

❌ Invalid Variable Names

```python
1name = "John"      # Cannot start with a number
my-age = 24         # Hyphen (-) is not allowed
class = "Python"    # Reserved keyword
```

### Best Practices

- Use meaningful names.
- Use `snake_case` for multiple words.
- Keep names short but descriptive.

Example:

```python
student_name = "Arindom"
total_marks = 95
```

---

# 📌 Data Types

Python automatically detects the data type of a variable.

| Data Type | Example |
|-----------|---------|
| `str` | `"Hello"` |
| `int` | `25` |
| `float` | `3.14` |
| `bool` | `True`, `False` |

Example:

```python
name = "Arindom"
age = 24
height = 5.8
is_student = True
```

---

# 📌 Printing Variables

```python
name = "Arindom"

print(name)
```

Output

```
Arindom
```

Print multiple variables:

```python
name = "Arindom"
age = 24

print(name)
print(age)
```

Output

```
Arindom
24
```

---

# 📌 Printing Text with Variables

```python
name = "Arindom"

print("My name is", name)
```

Output

```
My name is Arindom
```

---

# 📌 The input() Function

The `input()` function allows the user to enter data.

### Syntax

```python
input("Message")
```

Example:

```python
name = input("Enter your name: ")

print(name)
```

Output

```
Enter your name: Arindom
Arindom
```

---

# 📌 Important: input() Always Returns a String

```python
age = input("Enter your age: ")

print(type(age))
```

Output

```
<class 'str'>
```

Even if the user enters a number, Python stores it as **text**.

---

# 📌 Type Conversion

## Convert to Integer

```python
age = int(input("Enter your age: "))
```

## Convert to Float

```python
height = float(input("Enter your height: "))
```

## Convert to String

```python
number = 25

text = str(number)
```

---

# 📌 type() Function

Use `type()` to check the data type of a variable.

Example:

```python
name = "Arindom"
age = 24

print(type(name))
print(type(age))
```

Output

```
<class 'str'>
<class 'int'>
```

---

# 📌 Basic Calculator Example

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)
```

---

# 📌 Useful Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `5 + 2 = 7` |
| `-` | Subtraction | `5 - 2 = 3` |
| `*` | Multiplication | `5 * 2 = 10` |
| `/` | Division | `5 / 2 = 2.5` |
| `//` | Floor Division | `5 // 2 = 2` |
| `%` | Modulus (Remainder) | `5 % 2 = 1` |
| `**` | Exponent | `5 ** 2 = 25` |

---

# 📌 Mini Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("You are", age, "years old.")
```

---

# 📌 Common Errors

### Forgetting Type Conversion

❌

```python
age = input("Age: ")

next_year = age + 1
```

This will cause an error because `age` is a string.

✅

```python
age = int(input("Age: "))

next_year = age + 1
```

---

### Invalid Integer Input

❌

```python
age = int(input("Age: "))
```

If the user enters:

```
twenty
```

Python raises:

```
ValueError
```

---

# 📌 Key Takeaways

- Variables store data.
- Python has multiple data types (`str`, `int`, `float`, `bool`).
- `print()` displays output.
- `input()` receives user input.
- `input()` always returns a string.
- Use `int()`, `float()`, and `str()` for type conversion.
- Use `type()` to check a variable's data type.
- Follow good variable naming practices.

---

# 📚 Practice Ideas

- Create a personal profile program.
- Build a simple calculator.
- Calculate BMI.
- Calculate age in days.
- Build a Mad Libs game.
- Ask the user for favorite movies, books, or hobbies and display them in a formatted message.

---

## 💡 Remember

> **"Variables store information, and `input()` lets your program interact with users."**
