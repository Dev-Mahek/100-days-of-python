# Check if an Item Exists

numbers = [5, 10, 15, 20, 25]

if 15 in numbers:
    print("Found")
else:
    print("Not Found")

# Print Every Number

numbers = [3, 6, 9, 12, 15]

for num in numbers:
    print(num)

# Print Even Numbers

numbers = [3, 6, 9, 12, 15]

for num in numbers:
    if num % 2 == 0:
        print(num)

# Find the Largest Number Without max()

numbers = [3, 6, 9, 12, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
