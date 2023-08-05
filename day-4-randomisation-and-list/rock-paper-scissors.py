rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
hands = [rock, paper, scissors]
player_hand = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if (player_hand > 2) or (player_hand < 0):
  print("Your input is incorrect. You lose!")
else:
  print(hands[player_hand])
  
  print("Computer choose:")
  computer_hand = random.randint(0,2)
  print(hands[computer_hand])  
  
  if (player_hand == 2) and (computer_hand == 0):
    print("You lose!")
  elif (computer_hand == 2) and (player_hand == 0):
    print("You won!")
  elif player_hand > computer_hand:
    print("You won!")
  elif computer_hand > player_hand:
    print("You lose!")
  elif player_hand == computer_hand:
    print("It's a draw.")
  

# #Draw
# if player_hand == computer_hand:
#   print("It's a draw.")

# #Win
# if ((player_hand == 0) and (computer_hand == 2)) or ((player_hand == 1) and (computer_hand == 0)) or ((player_hand == 2) and (computer_hand == 1)):
#   print("You Won!")

# #Lose
# if ((player_hand == 0) and (computer_hand == 1)) or ((player_hand == 1) and (computer_hand == 2)) or ((player_hand == 2) and (computer_hand == 0)):
#   print("You Lose!")