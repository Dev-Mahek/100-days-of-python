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
