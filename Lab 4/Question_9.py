# Program should simulate rolling two dice about 10,000 times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . ,

import random

def DiceRollin():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    return dice_sum

def ComputeAndPrint():
    dice_sum_list = []
    for i in range(10000):
        dice_sum_list.append(DiceRollin())
    for i in range(2,13):
        print("The percentage of rolls that come out to be", i, "is", dice_sum_list.count(i)/100, "%")

# Driver Code
ComputeAndPrint()