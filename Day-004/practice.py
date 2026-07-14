age = 20

if age >= 18:
    print("You can vote.")


number = 10

if number == 10:
    print("Correct")


age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")


marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")


age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")


day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


logged_in = False

if not logged_in:
    print("Please log in.")


# ATM Login

pin = "1234"

user_pin = input("Enter your PIN: ")

if user_pin == pin:
    print("Login Successful")
else:
    print("Wrong PIN")


# Movie Ticket Checker

age = int(input("Enter your age: "))

if age < 5:
    print("Free Ticket")
elif age <= 17:
    print("Child Ticket")
elif age <= 59:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")
