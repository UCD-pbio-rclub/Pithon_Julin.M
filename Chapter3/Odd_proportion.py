#Using the random module and the examples in the book,
#simulate 1000 random single dice throws then print the proportion
#of odd numbered dice throws.
#(Optional: repeat using 3 dice in each throw and the sum of the dice)

import random

odd_total = 0
for throw in range(1,1001):
    dice1 = random.randint(1,6)
    if (dice1 % 2 != 0):
        odd_total = odd_total + 1
odd_proportion = odd_total/1000

print("Proportion of odd throws:", odd_proportion)
    
