"""
Build a Restaurant Bill Discount Calculator.

Requirements:

Ask the user to enter the bill amount.
If the bill is ₹5000 or more, give a 20% discount.
Else if the bill is ₹2000 or more, give a 10% discount.
Otherwise, give no discount.
Print:
Original bill
Discount amount
Final amount to pay

Example:

Enter bill amount: 3500

Original Bill: ₹3500
Discount: ₹350
Final Bill: ₹3150
"""

bill = float(input("Enter your bill amount: ₹"))

if bill >= 5000:
    discount = bill * 0.20
elif bill >= 2000:
    discount = bill * 0.10
else:
    discount = 0

final_bill = bill - discount

print("\n----- BILL SUMMARY -----")
print(f"Original Bill : ₹{bill:.2f}")
print(f"Discount      : ₹{discount:.2f}")
print(f"Final Bill    : ₹{final_bill:.2f}")
