#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
total_bill_int = float(total_bill)
# print(total_bill_int)
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
final_tip = round(tip_percent/100 , 2) + 1
# print(final_tip)
bill_split = int(input("How many people to split the bill? "))
bill_division = (total_bill_int / bill_split) * (final_tip)
final_bill = (round(bill_division, 2))
print(f"Each person should pay ${final_bill}")