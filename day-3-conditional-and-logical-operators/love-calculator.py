# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

## MY SOLUTION
#set name1 & name2 to all lower case
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

count_t = lower_case_name1.count("t") + lower_case_name2.count("t")
count_r = lower_case_name1.count("r") + lower_case_name2.count("r")
count_u = lower_case_name1.count("u") + lower_case_name2.count("u")
count_e = lower_case_name1.count("e") + lower_case_name2.count("e")

count_l = lower_case_name1.count("l") + lower_case_name2.count("l")
count_o = lower_case_name1.count("o") + lower_case_name2.count("o")
count_v = lower_case_name1.count("v") + lower_case_name2.count("v")
count_e = lower_case_name1.count("e") + lower_case_name2.count("e")

sum_of_true = count_t + count_r + count_u + count_e
sum_of_love = count_l + count_o + count_v + count_e

score = str(sum_of_true) + str(sum_of_love)
score = int(score)

if (score < 10 )or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")



#Solution in the video
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10 )or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

