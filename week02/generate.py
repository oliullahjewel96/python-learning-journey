import random
# from random import choice

# coin = choice(["heads","tails"])
# coin = random.choice(["heads","tails"])

# rand_number = random.randint(1,100)

cards = ['Jack', 'King', 'Queen', 'Ace','1','2','3','4','5','6','7','8','9']

random.shuffle(cards)

for card in cards:
    print(card)

# print(rand_number)