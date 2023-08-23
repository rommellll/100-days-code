# file = open("hello.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("/Users/codingchiefs/PycharmProjects/day-20-snake-game/data.txt") as file:
    contents = file.read()
    print(contents)


with open("new-file.txt",mode="a") as file:
    file.write("\nNew text.")
