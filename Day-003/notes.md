# ⚡ Python Operators

> Operators are special symbols used to perform operations on variables and values.

---

# 📖 Table of Contents

* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Operator Precedence
* Practice Questions
* Mini Project
* Key Takeaways

---

# ➕ 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name                | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 2`  | `7`    |
| `-`      | Subtraction         | `5 - 2`  | `3`    |
| `*`      | Multiplication      | `5 * 2`  | `10`   |
| `/`      | Division            | `5 / 2`  | `2.5`  |
| `//`     | Floor Division      | `5 // 2` | `2`    |
| `%`      | Modulus (Remainder) | `5 % 2`  | `1`    |
| `**`     | Exponent            | `5 ** 2` | `25`   |

### Example

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
```

### Output

```text
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponent: 1000
```

---

# 📝 2. Assignment Operators

Assignment operators assign or update the value of a variable.

## Basic Assignment

```python
x = 10
```

## Shortcut Assignment

| Operator | Equivalent       |
| -------- | ---------------- |
| `+=`     | `x = x + value`  |
| `-=`     | `x = x - value`  |
| `*=`     | `x = x * value`  |
| `/=`     | `x = x / value`  |
| `//=`    | `x = x // value` |
| `%=`     | `x = x % value`  |
| `**=`    | `x = x ** value` |

### Example

```python
score = 50

score += 10
score -= 5
score *= 2

print(score)
```

### Output

```text
110
```

---

# ⚖️ 3. Comparison Operators

Comparison operators compare two values.

The result is always either:

* `True`
* `False`

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
age = 20

print(age == 20)
print(age != 20)
print(age > 18)
print(age < 18)
```

### Output

```text
True
False
True
False
```

---

# 🧠 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning                                          |
| -------- | ------------------------------------------------ |
| `and`    | Returns `True` if both conditions are true       |
| `or`     | Returns `True` if at least one condition is true |
| `not`    | Reverses the result                              |

### Example

```python
age = 22
student = True

print(age > 18 and student)
print(age < 18 or student)
print(not student)
```

### Output

```text
True
True
False
```

---

# 🪞 5. Identity Operators

Identity operators check whether two variables refer to the **same object in memory**.

| Operator | Meaning           |
| -------- | ----------------- |
| `is`     | Same object       |
| `is not` | Different objects |

### Example

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)
```

### Output

```text
True
False
True
```

> **Remember**
>
> * `==` compares values.
> * `is` compares object identity.

---

# 📦 6. Membership Operators

Membership operators check whether an item exists in a sequence.

| Operator | Meaning             |
| -------- | ------------------- |
| `in`     | Item exists         |
| `not in` | Item does not exist |

### Example

```python
fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)
```

### Output

```text
True
False
True
```

---

# ⭐ 7. Operator Precedence

Python follows a specific order when evaluating expressions.

| Priority | Operator             |
| -------- | -------------------- |
| 1        | `()` Parentheses     |
| 2        | `**` Exponent        |
| 3        | `*`, `/`, `//`, `%`  |
| 4        | `+`, `-`             |
| 5        | Comparison Operators |
| 6        | `not`                |
| 7        | `and`                |
| 8        | `or`                 |

### Example

```python
result = 5 + 3 * 2
print(result)
```

Output

```text
11
```

Because multiplication happens before addition.

---

# 🏋️ Practice Questions

## Question 1

```python
x = 15
y = 4

print(x + y)
print(x // y)
print(x % y)
```

---

## Question 2

```python
money = 100

money += 50
money -= 20
money *= 2

print(money)
```

---

## Question 3

```python
a = 25
b = 30

print(a > b)
print(a != b)
print(a >= 25)
```

---

## Question 4

```python
x = 10

print(x > 5 and x < 20)
print(x > 20 or x == 10)
print(not x == 10)
```

---

# 🚀 Mini Project — Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)
```

### 💡 Challenge

Extend this calculator by displaying:

* Which number is greater.
* Whether both numbers are equal.
* Whether one number is divisible by the other.

---

# 🎯 Key Takeaways

* Operators perform actions on variables and values.
* Arithmetic operators are used for calculations.
* Assignment operators update variable values.
* Comparison operators always return `True` or `False`.
* Logical operators combine conditions.
* Identity operators compare objects in memory.
* Membership operators check whether an item exists in a collection.
* Parentheses `()` have the highest precedence and can make expressions easier to read.

---

# 📚 What's Next?

➡️ **Conditional Statements (`if`, `elif`, `else`)**

Operators become much more useful when combined with decision-making in Python programs.
