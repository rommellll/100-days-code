# adding 1 to an existing list of number
numbers = [1, 2, 3, 4, 5]
new_num = [n + 1 for n in numbers]

# iterating to a string
name = "rommel"
letters = [letter for letter in name]

# using range
numbers = [n * 2 for n in range(1, 5)]

# conditional list comprenhesion
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [nickname for nickname in names if len(nickname) < 5]
print(short_names)

upper_case_name = [name.upper() for name in names if len(name) > 5]
print(upper_case_name)

# # dictionary comprehension
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {student:random.randint(1,100) for student in names}
# passed_students = {students:score for (students,score) in student_score.items() if score > 60}

# looping through dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 87]
}

for (key, value) in student_dict.items():
    print(value)

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# loop through data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through each row of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)