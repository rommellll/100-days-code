import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

bids = {}
continue_bidding = True

def find_the_highest_bidder(bidding_record):
  winning_bid = 0
  for bidder in bidding_record:
      bid = bids[bidder]
      if bid > winning_bid:
        winning_bid = bid
        winning_person = bidder
  print(f"The winner is {winning_person} with a bid of ${winning_bid}")
    
while continue_bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid? $"))
  bids[name] = bid
  answer = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  os.system('cls' if os.name == 'nt' else 'clear')
  if answer == "no":
    continue_bidding = False
    find_the_highest_bidder(bids)
    
  
