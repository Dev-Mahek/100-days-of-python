"""
Given

language = "Programming"

Print

First letter
Last letter
Third letter
Second last letter
"""

language = "Programming"

print(language[0])
print(language[-1])
print(language[2])
print(language[-2])

"""
Given

name = "Arindom"

Print

"Ari"
"dom"
Reverse the name
Every second character
"""

name = "Arindom"

print(name[:3])     # Ari
print(name[4:])     # dom
print(name[::-1])   # modnirA
print(name[::2])    # Aido

"""
Given

sentence = "   i love python programming   "

Perform the following:

Remove extra spaces.
Convert to title case.
Replace "Python" with "R".
Count how many "m" characters are in the result.
"""

sentence = "   i love python programming   "

sentence = sentence.strip()
sentence = sentence.title()
sentence = sentence.replace("Python", "R")

print(sentence)

count = sentence.lower().count("m")
print("Number of m:", count)

# I Love R Programming
# Number of m: 2

"""
Write a program that asks the user for:

Name
Age
College
Course

Then print a neat ID card.

Example output:

========================
      STUDENT ID
========================
Name    : Arindom Roy
Age     : 23
College : XYZ College
Course  : MBA
========================

Use f-strings for formatting.
"""

name = input("Enter your name: ")
age = input("Enter your age: ")
college = input("Enter your college: ")
course = input("Enter your course: ")

print("========================")
print("       STUDENT ID")
print("========================")

print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"College : {college}")
print(f"Course  : {course}")

print("========================")
