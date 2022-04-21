# Program to Make 10 x 10 List of random numbers between 1 and 100.

import random

RandomList = [[random.randint(1,100) for i in range(10)] for j in range(10)]
print(RandomList)

# Find the largest value in the third row.
Largest = max(RandomList[2])
print(Largest)

#  Find the smallest value in the sixth column
Smallest = min(RandomList[5])
print(Smallest)