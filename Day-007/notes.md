# 📚 Python Lists - Complete Notes

> Beginner-friendly notes for learning Python Lists with examples.

---

# 📖 What is a List?

A **list** is a built-in Python data structure used to store **multiple values** in a single variable.

Lists are:

- ✅ Ordered
- ✅ Mutable (can be changed)
- ✅ Allow duplicate values
- ✅ Can store different data types

### Example

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

# Creating Lists

### Empty List

```python
students = []
```

### List of Numbers

```python
numbers = [10, 20, 30, 40]
```

### List of Strings

```python
colors = ["Red", "Blue", "Green"]
```

### Mixed Data Types

```python
data = ["Arindom", 21, True, 95.5]
```

---

# Indexing

Lists use **zero-based indexing**.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]
```

| Index | Value |
|-------:|--------|
| 0 | Apple |
| 1 | Banana |
| 2 | Mango |
| 3 | Orange |

### Access First Element

```python
print(fruits[0])
```

Output

```text
Apple
```

### Access Last Element

```python
print(fruits[-1])
```

Output

```text
Orange
```

---

# Modifying List Items

Lists are **mutable**, meaning items can be changed.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Grapes"

print(fruits)
```

Output

```text
['Apple', 'Grapes', 'Mango']
```

---

# Adding Items

## append()

Adds an item to the **end** of the list.

```python
fruits.append("Orange")
```

Output

```python
['Apple', 'Banana', 'Mango', 'Orange']
```

---

## insert()

Adds an item at a specific index.

```python
fruits.insert(1, "Kiwi")
```

Output

```python
['Apple', 'Kiwi', 'Banana', 'Mango']
```

---

# Removing Items

## remove()

Removes an item by **value**.

```python
fruits.remove("Banana")
```

---

## pop()

Removes the **last item**.

```python
fruits.pop()
```

---

## pop(index)

Removes an item using its index.

```python
fruits.pop(1)
```

---

## clear()

Removes every item.

```python
fruits.clear()
```

Output

```python
[]
```

---

# Useful Built-in Functions

```python
numbers = [5, 10, 15, 20]
```

## Length

```python
len(numbers)
```

Output

```text
4
```

---

## Maximum

```python
max(numbers)
```

Output

```text
20
```

---

## Minimum

```python
min(numbers)
```

Output

```text
5
```

---

## Sum

```python
sum(numbers)
```

Output

```text
50
```

---

# Membership Operator

Check whether an item exists.

```python
if "Apple" in fruits:
    print("Found")
else:
    print("Not Found")
```

---

# Looping Through a List

```python
fruits = ["Apple", "Banana", "Mango"]
```

```python
for fruit in fruits:
    print(fruit)
```

Output

```text
Apple
Banana
Mango
```

---

# Loop Using Index

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

Output

```text
0 Apple
1 Banana
2 Mango
```

---

# Finding the Largest Number (Without max())

```python
numbers = [3, 6, 9, 12, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
```

Output

```text
15
```

---

# Common List Methods

| Method | Description |
|---------|-------------|
| `append(x)` | Add item to end |
| `insert(i, x)` | Insert at index |
| `remove(x)` | Remove by value |
| `pop()` | Remove last item |
| `pop(i)` | Remove by index |
| `sort()` | Sort list ascending |
| `sort(reverse=True)` | Sort descending |
| `reverse()` | Reverse list |
| `count(x)` | Count occurrences |
| `index(x)` | Find index of value |
| `copy()` | Copy list |
| `clear()` | Remove all items |

---

# Sorting Lists

## Ascending

```python
numbers = [4, 2, 9, 1]

numbers.sort()

print(numbers)
```

Output

```text
[1, 2, 4, 9]
```

---

## Descending

```python
numbers.sort(reverse=True)
```

Output

```text
[9, 4, 2, 1]
```

---

# Reversing a List

```python
numbers.reverse()
```

---

# Copying a List

```python
new_list = numbers.copy()
```

---

# Counting Elements

```python
numbers = [1, 2, 2, 2, 3]

print(numbers.count(2))
```

Output

```text
3
```

---

# Finding the Index

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))
```

Output

```text
1
```

---

# Nested Lists

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Access an element:

```python
print(matrix[1][0])
```

Output

```text
3
```

---

# List Slicing

```python
numbers = [10, 20, 30, 40, 50]
```

First three elements

```python
numbers[:3]
```

Output

```python
[10, 20, 30]
```

Last two elements

```python
numbers[-2:]
```

Output

```python
[40, 50]
```

---

# List Concatenation

```python
list1 = [1, 2]
list2 = [3, 4]

result = list1 + list2
```

Output

```python
[1, 2, 3, 4]
```

---

# Repeating a List

```python
numbers = [1, 2]

print(numbers * 3)
```

Output

```python
[1, 2, 1, 2, 1, 2]
```

---

# Common Mistakes

### ❌ Wrong Index

```python
fruits[10]
```

Error:

```text
IndexError
```

---

### ❌ Removing a Value That Doesn't Exist

```python
fruits.remove("Kiwi")
```

Error:

```text
ValueError
```

Always check first:

```python
if "Kiwi" in fruits:
    fruits.remove("Kiwi")
```

---

# Best Practices

- Use meaningful variable names.
- Prefer `append()` when adding to the end.
- Use `remove()` when you know the value.
- Use `pop()` when you know the index.
- Use loops to process lists.
- Avoid modifying a list while iterating over it unless you understand the consequences.

---

# Interview Questions

### Q1. Are lists mutable?

✅ Yes.

---

### Q2. Can lists store different data types?

✅ Yes.

```python
data = ["John", 25, True, 90.5]
```

---

### Q3. Difference between `append()` and `insert()`?

| append() | insert() |
|-----------|----------|
| Adds to end | Adds at specific index |

---

### Q4. Difference between `remove()` and `pop()`?

| remove() | pop() |
|-----------|-------|
| Removes by value | Removes by index |
| Returns nothing | Returns removed value |

---

# Cheat Sheet

```python
my_list = []

my_list.append(x)
my_list.insert(i, x)
my_list.remove(x)
my_list.pop()
my_list.pop(i)

len(my_list)
max(my_list)
min(my_list)
sum(my_list)

x in my_list

my_list.sort()
my_list.sort(reverse=True)
my_list.reverse()

my_list.count(x)
my_list.index(x)

my_list.copy()
my_list.clear()

for item in my_list:
    print(item)
```

---

# Practice Exercises

1. Create a list of five fruits and print the second fruit.
2. Replace the third fruit with `"Pineapple"`.
3. Add two new fruits using `append()`.
4. Insert `"Kiwi"` at index `2`.
5. Remove `"Banana"` from the list.
6. Print the largest and smallest numbers from a list.
7. Count how many times `5` appears in a list.
8. Reverse a list.
9. Sort a list in descending order.
10. Find the largest number without using `max()`.

---

# Summary

Python Lists are one of the most important data structures because they let you:

- Store multiple values
- Access items using indexes
- Modify data easily
- Add and remove elements
- Loop through collections
- Sort and search data
- Build real-world applications like shopping carts, student managers, quizzes, and inventory systems
