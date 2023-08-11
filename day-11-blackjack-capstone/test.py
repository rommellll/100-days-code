import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

for _ in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

player_score = sum(player_cards)
computer_score = sum(computer_cards)

while player_score < 30:
    player_cards.append(random.choice(cards))
    print(player_cards)
    player_score = sum(player_cards)