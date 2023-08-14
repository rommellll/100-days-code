import os
import random

from art import logo, vs
from game_data import data

print(logo)


def celebrity_detail(celebrity):
    """
    Generate an intro from the celebrity dictionary
    """
    name = celebrity["name"]
    followers = celebrity["follower_count"]
    description = celebrity["description"]
    country = celebrity["country"]
    intro = f"{name}, a {description}, from {country}"
    return intro


def compare_celebrity(A, B):
    if A > B:
        return "A"
    else:
        return "B"


def game():
    is_game_end = False
    score = 0
    celebrity_1 = random.choice(data)
    while not is_game_end:
        celebrity_2 = random.choice(data)
        # while both celebrity is the same, change celebrity_2
        while celebrity_1 == celebrity_2:
            celebrity_2 = random.choice(data)

        detail = (celebrity_detail(celebrity=celebrity_1))
        A = celebrity_1["follower_count"]
        print(f"Compare A: {detail}")
        print(vs)
        detail = (celebrity_detail(celebrity=celebrity_2))
        B = celebrity_2["follower_count"]
        print(f"Againts b: {detail}")
        print(f"{A} vs {B}")
        winner = compare_celebrity(A, B)
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == winner:
            score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"You're right! Current score: {score}")
            if answer == "B":
                celebrity_1 = celebrity_2
        else:
            is_game_end = True
            print(f"Sorry, that's wrong. Your final score: {score}")


game()
