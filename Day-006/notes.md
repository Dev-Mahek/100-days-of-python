# 🔁 Python `for` Loops

The `for` loop is used to repeat a block of code for each item in a sequence, such as a list, tuple, string, or range.

---

# 📖 Syntax

```python
for variable in sequence:
    # Code to execute
```

- **`variable`** → Stores the current item during each iteration.
- **`sequence`** → A list, tuple, string, dictionary, or `range()`.
- The indented code runs once for every item in the sequence.

---

# 🧠 How a `for` Loop Works

Python takes one item from the sequence at a time and assigns it to the loop variable.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Banana
Mango
```

### Execution

```
fruit = "Apple"
↓

print("Apple")

↓

fruit = "Banana"
↓

print("Banana")

↓

fruit = "Mango"
↓

print("Mango")
```

---

# 🔢 Using `range()`

The `range()` function generates a sequence of numbers.

## `range(stop)`

```python
for i in range(5):
    print(i)
```

Output

```text
0
1
2
3
4
```

---

## `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
```

Output

```text
2
3
4
5
```

---

## `range(start, stop, step)`

```python
for i in range(0, 11, 2):
    print(i)
```

Output

```text
0
2
4
6
8
10
```

---

# 📝 Printing a Message Multiple Times

```python
for i in range(5):
    print("I love Python")
```

Output

```text
I love Python
I love Python
I love Python
I love Python
I love Python
```

---

# ➕ Finding the Sum of Numbers

```python
marks = [78, 92, 85, 66, 90]

total = 0

for mark in marks:
    total += mark

print(total)
```

Output

```text
411
```

---

# ✖️ Multiplying Values

```python
numbers = [2, 4, 6, 8]

for number in numbers:
    print(number * 2)
```

Output

```text
4
8
12
16
```

---

# 🔤 Looping Through a String

```python
name = "Python"

for letter in name:
    print(letter)
```

Output

```text
P
y
t
h
o
n
```

---

# 💡 Useful Tips

- A `for` loop automatically stops when it reaches the end of the sequence.
- The loop variable can have any meaningful name.

```python
for student in students:
```

is better than

```python
for x in students:
```

unless you're working with numbers.

---

# ⚠️ Common Mistakes

### ❌ Forgetting the colon

```python
for i in range(5)
```

✅ Correct

```python
for i in range(5):
```

---

### ❌ Incorrect indentation

```python
for i in range(5):
print(i)
```

✅ Correct

```python
for i in range(5):
    print(i)
```

---

### ❌ Modifying the loop variable

```python
for i in range(5):
    i = 100
```

Changing `i` inside the loop does **not** affect how the loop iterates.

---

# 🎯 Key Takeaways

- `for` loops repeat code automatically.
- They work with lists, tuples, strings, dictionaries, and `range()`.
- `range()` is commonly used to repeat code a specific number of times.
- Always end the `for` statement with a colon (`:`).
- Indentation is required inside the loop.
- Use meaningful variable names for better readability.

---

## 🚀 Practice Exercises

- Print every item in a list.
- Print numbers from 1 to 10.
- Print even numbers between 1 and 20.
- Find the sum of a list.
- Find the largest number in a list.
- Count vowels in a string.
- Print a multiplication table.
- Print a star (`*`) pattern using nested loops.

---

**Happy Coding! 🐍**
