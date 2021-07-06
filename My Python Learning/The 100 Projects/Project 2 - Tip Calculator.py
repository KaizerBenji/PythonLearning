# Project 2 Tip Calculator
print("The Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What % tip would you like to leave? 10, 15, 20? "))
people = int(input("How many people are splitting the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_total = "{:.2f}".format(bill_per_person)
print(f"Each person will pay ${final_total}.")

