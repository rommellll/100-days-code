# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
#Write your code below this row 👇
num_of_students = 0
sum_of_heights = 0
for heights in student_heights:
    num_of_students += 1
    sum_of_heights += heights

average_height = round(sum_of_heights / num_of_students)

#print(f"There are a total of {num_of_students} students in {average_height}")
print(average_height)


#what can be done using len and sum functions.
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)