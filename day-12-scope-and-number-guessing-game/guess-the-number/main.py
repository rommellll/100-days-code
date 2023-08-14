import random

def set_lives(difficulty):
    """
    Set number of guesses base on selected difficulty.
    """
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        exit("You provided incorrect input.")
    
def check_guess(player_guess,random_number):
    if player_guess == random_number:
        print(f"You got it! The answer was {random_number}")
        return True
    elif player_guess > random_number:
        print("Too high.")
    elif player_guess < random_number:
        print("Too low.")
    print("Guess again.")
    return False
    
def game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1,100)
    print("I'm thinking a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guesses = set_lives(level)
    is_game_end = False
    while not is_game_end:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess.: "))
        is_game_end = check_guess(player_guess=guess,random_number=number)
        guesses -= 1
        if guesses == 0 and not is_game_end:
            print("You've run out of guesses. You lose.")
            is_game_end = True

game()