print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
price = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        price = 5
        print("Your ticket price is $5")
    elif age <= 18:
        price = 7
        print("Your ticket price is $7")
    else:
        price = 12
        print("Your ticket price is $12")
    
    #check if they want photo
    wants_photo = input("Do you want photo for additional $3? Y or N. ")
    if wants_photo == "Y":
        price += 3
    
    print(f"Your final bill is ${price}")
else:
    print("you cant ride")