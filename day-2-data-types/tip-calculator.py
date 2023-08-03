#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
person = int(input("How many person would split the bill? "))

total_tip = bill * (tip / 100)
total_bill = bill + total_tip
split_bill = round(total_bill / person, 2)
split_bill = "{:.2f}".format(split_bill)
message = f"Each person should pay: ${split_bill}"

print(message)