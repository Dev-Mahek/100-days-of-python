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
