print("welcome to TIP calculator")
bill = float(input("What was total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 ?\n"))
people = int((input("How many people to split bill?\n")))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"each person would pay: ${final_amount}")
