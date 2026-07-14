name = "Arindom"
country = 'India'

print(name)
print(country)


text = """Python
is
awesome"""

print(text)


# Indexing

word = "Python"

print(word[0])
print(word[1])
print(word[5])

print(word[-1])
print(word[-2])


# Slicing

text = "Programming"

print(text[0:4])

text = "Programming"

print(text[3:7])

word = "Programming"

print(word[::2])

word = "Python"

print(word[::-1])


# String Length

name = "Python"

print(len(name))


# Common String Methods

# Uppercase
name = "arindom"

print(name.upper())

# Lowercase
print(name.lower())

# Title Case
text = "i love python"

print(text.title())
# Capitalize
print(text.capitalize())

# Replace
sentence = "I love Java"

print(sentence.replace("Java", "Python"))

# Count
word = "banana"

print(word.count("a"))

# Find
word = "Programming"

print(word.find("g"))

# Startswith
word = "Python"

print(word.startswith("Py"))

# Endswith
print(word.endswith("on"))

# Strip
text = "   hello   "

print(text.strip())

# Split
sentence = "I love Python"

print(sentence.split())

# Join
words = ["I", "love", "Python"]

print(" ".join(words))


# Concatenation

first = "Hello"
second = "World"

print(first + " " + second)

# Membership

text = "Python"

print("Py" in text)
print("Java" in text)

# Escape Characters

print("He said \"Hello\"")
# He said "Hello"

print("Hello\nWorld")
"""
Hello
World
"""

# String Formatting Old Way
name = "Arindom"

print("Hello " + name)

# Better Way (f-strings)
name = "Arindom"
age = 23

print(f"My name is {name} and I am {age} years old.")
# My name is Arindom and I am 23 years old.
