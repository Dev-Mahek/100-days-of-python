# Arithmetic Operators

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Assignment Operators

score = 50

score += 10
print(score)

money = 100

money += 50
money -= 20
money *= 2
money //= 5

print(money)

# Comparison Operators

"""
True
or
False
"""

age = 20

print(age == 20)
print(age != 20)
print(age > 18)
print(age < 18)

# Logical Operators

age = 22
student = True

print(age > 18 and student)

print(age < 18 or student)

print(not student)

age = 22
student = True

print(age > 18 and student)

print(age < 18 or student)

print(not student)

# Identity Operators (is, is not)

a = [1, 2]

b = a

c = [1, 2]

print(a is b)

print(a is c)

print(a == c)

# Membership Operators (in, not in)

fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)

print("Orange" in fruits)

print("Orange" not in fruits)
