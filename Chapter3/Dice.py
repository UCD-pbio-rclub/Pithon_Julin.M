import random
for x in range(1,11):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print("the the total is:", total)
    if (total == 7 or total == 11):
        print("Wow! a", total, "was thrown")
    if (dice1 == dice2):
        print("Wow, a double:",dice1,"+",dice2)
    if (total > 10):
        print("Good throw!")
    if (total < 4):
        print("Bad luck!")
