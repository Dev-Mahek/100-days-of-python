# Python Strings Notes

## 1. What is a String?

A string is a sequence of characters enclosed inside quotes.

```python
name = "Arindom"
city = 'Silchar'
```

Both single (`' '`) and double (`" "`) quotes can be used.

---

# 2. Creating Multi-line Strings

Use triple quotes:

```python
text = """
Python
is
awesome
"""
```

---

# 3. String Indexing

Each character has an index position.

Example:

```
P  y  t  h  o  n
0  1  2  3  4  5
```

Negative indexing:

```
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

Example:

```python
word = "Python"

print(word[0])   # P
print(word[-1])  # n
```

---

# 4. String Slicing

Syntax:

```python
string[start:end]
```

The ending index is not included.

Example:

```python
text = "Programming"

print(text[0:4])
```

Output:

```
Prog
```

### Useful slicing examples:

```python
text[:5]      # From beginning
text[5:]      # Until end
text[:]       # Full string
text[::2]     # Every second character
text[::-1]    # Reverse string
```

Example:

```python
name = "Arindom"

print(name[:3])     # Ari
print(name[4:])     # dom
print(name[::-1])   # modnirA
print(name[::2])    # Aido
```

---

# 5. String Length

Use `len()`:

```python
name = "Python"

print(len(name))
```

Output:

```
6
```

---

# 6. Important String Methods

## upper()

Converts string to uppercase.

```python
name = "arindom"

print(name.upper())
```

Output:

```
ARINDOM
```

---

## lower()

Converts string to lowercase.

```python
print("PYTHON".lower())
```

Output:

```
python
```

---

## title()

Converts first letter of every word to uppercase.

```python
text = "i love python"

print(text.title())
```

Output:

```
I Love Python
```

---

## capitalize()

Capitalizes only the first letter.

```python
text = "python"

print(text.capitalize())
```

Output:

```
Python
```

---

## replace()

Replace one word with another.

```python
text = "I love Java"

print(text.replace("Java", "Python"))
```

Output:

```
I love Python
```

---

## count()

Counts occurrences of characters.

```python
word = "banana"

print(word.count("a"))
```

Output:

```
3
```

---

## find()

Finds the position of a character.

```python
text = "Programming"

print(text.find("g"))
```

Output:

```
3
```

Returns `-1` if not found.

---

## startswith()

Checks beginning of string.

```python
text = "Python"

print(text.startswith("Py"))
```

Output:

```
True
```

---

## endswith()

Checks ending of string.

```python
text = "Python"

print(text.endswith("on"))
```

Output:

```
True
```

---

## strip()

Removes extra spaces.

```python
text = "   hello   "

print(text.strip())
```

Output:

```
hello
```

---

## split()

Converts string into a list.

```python
sentence = "I love Python"

print(sentence.split())
```

Output:

```
['I', 'love', 'Python']
```

---

## join()

Combines list items into a string.

```python
words = ["I", "love", "Python"]

print(" ".join(words))
```

Output:

```
I love Python
```

---

# 7. String Operators

## Concatenation (+)

Joining strings:

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```
Hello World
```

---

## Repetition (*)

```python
print("Hi " * 3)
```

Output:

```
Hi Hi Hi
```

---

## Membership (in)

Checks if a value exists.

```python
text = "Python"

print("Py" in text)
```

Output:

```
True
```

---

# 8. Escape Characters

## New Line

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

---

## Tab Space

```python
print("Python\tJava")
```

Output:

```
Python    Java
```

---

## Double Quotes

```python
print("He said \"Hello\"")
```

Output:

```
He said "Hello"
```

---

# 9. f-Strings

The modern way to format strings.

Syntax:

```python
f"Text {variable}"
```

Example:

```python
name = "Arindom"
age = 23

print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Arindom and I am 23 years old.
```

---

# 10. Real-life Project Example

## Student ID Card Generator

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
college = input("Enter your college: ")
course = input("Enter your course: ")

id_card = f"""
========================
       STUDENT ID
========================
Name    : {name}
Age     : {age}
College : {college}
Course  : {course}
========================
"""

print(id_card)
```

---
