# Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros, the largest number of zeros in a row. For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random

# Function to generate the list of 100 random integers
def Solution():
    List = []
    result = count = 0
    for i in range(100):
        List.append(random.randint(0,1))
    print("The list is: ", List)

    for i in range(len(List)):
        if List[i] == 0:
            count += 1
        else:
            if count > result:
                result = count
            count = 0
    print("The longest run of zeros is: ", result)

# Driver Code
Solution()