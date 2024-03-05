bill_price = input("What was the total bill? :" )
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = int(input("How many people to split the bill? "))

bill_price_float = float(bill_price)
tip_percent = int(tip) / 100
total_tip_amount = tip_percent * bill_price_float
total_bill = total_tip_amount + bill_price_float
total_for_each = ( total_bill / people) 

print(round(total_for_each))