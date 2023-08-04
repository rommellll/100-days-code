# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#classification = "empty"
bmi = round(weight / height ** 2)
#message = f"Your BMI is {bmi}, you are {classification}."
if bmi <= 18.5:
    classification = "underweight"
    message = f"Your BMI is {bmi}, you are {classification}."
    print(message)
elif bmi < 25:
    classification = "normal weight"
    message = f"Your BMI is {bmi}, you have a {classification}."
    print(message)
elif bmi < 30:
    classification = "slightly overweight"
    message = f"Your BMI is {bmi}, you are {classification}."
    print(message)
elif bmi < 35:
    classification = "obese"
    message = f"Your BMI is {bmi}, you are {classification}."
    print(message)
else:
    classification = "clinically obese"
    message = f"Your BMI is {bmi}, you are {classification}."
    print(message)