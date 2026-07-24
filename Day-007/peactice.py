fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

print(fruits[0])
print(fruits[-1])

fruits[1] = "Grapes"

print(fruits)


fruits.append("Orange")
fruits.append("Kiwi")


fruits.insert(1, "Pineapple")

print(fruits)

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)

print(numbers)


numbers.pop()

print(numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

