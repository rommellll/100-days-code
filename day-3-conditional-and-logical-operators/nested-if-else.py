print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket price is $5")
    elif age <= 18:
        print("Your ticket price is $7")
    else:
        print("Your ticket price is $12")
else:
    print("you cant ride")