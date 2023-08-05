# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

number_of_persons = len(names)
random_number = random.randint(1, (number_of_persons - 1))
loser = names[random_number]
print(f"{loser} is going to buy the meal today!")