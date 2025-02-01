total = float(input("What was the total bill?\n"))
tip_amount = int(input("How much would you like to tip? 10 , 12 or 15\n"))
split = int(input("How many people are you spliting the bill?\n"))
Calculate_billwithtip= total*(tip_amount/100) + total
bill_per_person = Calculate_billwithtip / split
final_amount = round(bill_per_person, 2)
print(f"Each person should pay:  ${final_amount}")