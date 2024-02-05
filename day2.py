# bill split calculator
print("Wel come to the tip-calculator")
bill = int(input("What was the total bill:"))
print(bill)
tip = int(input("Whhat percentage tip would you like to give: 10,12,15, or 20"))
tip_percent = (bill/100) * tip
tip_int = int(tip_percent)
total_bill = bill + tip_int
final = int(input("How many people to split the bill: "))
for_Each = total_bill / final
round_up = int(for_Each)
print(f"Each one have to pay $ {round_up} amount")
