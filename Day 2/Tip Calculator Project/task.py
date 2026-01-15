print("Welcome to the calculator!")
total_bill = float(input("What was the total  bills? $"))
tip_given_by  = int(input("How much tip would you like to give? 10, 12,or 15?"))
split_the_bill = int(input("How many to split the bill?"))
bill_with_tip = tip_given_by / 100 * total_bill + total_bill
print(bill_with_tip)

