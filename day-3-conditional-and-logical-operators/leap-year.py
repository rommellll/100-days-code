# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

condition1 = year % 4
condition2 = year % 100
condition3 = year % 400

if condition2 == 0 and condition3 !=0:
    print("Not leap year.")
elif condition1 == 0 or condition3 == 0:
    print("Leap year.")
else:
    print("Not leap year.")


# solution in the video

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# condition1 = year % 4
# condition2 = year % 100
# condition3 = year % 400

# if condition1 == 0:
#     if condition2 != 0:
#         print("Leap year.")
#     elif condition3 == 0:
#         print("Leap year.")
#     else:
#         print("Not a leap year.")
# else:
#     print("Not a leap year.")