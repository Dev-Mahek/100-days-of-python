"""
EMI Calculator
"""

loan = float(input("Enter loan amount: "))
months = int(input("Enter number of months: "))

emi = loan / months

print("Loan Amount:", loan)
print("Months:", months)
print("Monthly EMI: ₹", round(emi, 2))

"""
Tip Calculator
"""

bill = float(input("Enter Bill Amount: ₹"))
tip_percentage = float(input("Enter Tip Percentage (%): "))

tip_amount = bill * tip_percentage / 100
total_bill = bill + tip_amount

print("Bill Amount : ₹", bill)
print("Tip Amount  : ₹", round(tip_amount, 2))
print("Total Bill  : ₹", round(total_bill, 2))

"""
Shopping Bill Calculator
"""

item1 = float(input("Enter price of Item 1: ₹"))
item2 = float(input("Enter price of Item 2: ₹"))
item3 = float(input("Enter price of Item 3: ₹"))

subtotal = item1 + item2 + item3

gst = subtotal * 0.18

if subtotal > 5000:
    discount = subtotal * 0.10
else:
    discount = 0

final_bill = subtotal + gst - discount

print("Subtotal : ₹", subtotal)
print("GST (18%): ₹", gst)
print("Discount : ₹", discount)
print("Final Bill: ₹", round(final_bill, 2))
