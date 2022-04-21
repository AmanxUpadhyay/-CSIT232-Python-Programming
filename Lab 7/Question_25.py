# There is only one five-digit number n that is such that every one of the following ten numbers shares exactly one digit in common in the same position as n. Find n.

import random

def Solution():
    # Generate a list of 10 numbers.
    List = []
    for i in range(10):
        List.append(random.randint(10000, 99999))

    print("List:", List)
    # Check if the number is a five-digit number.
    for i in range(10):
        if len(str(List[i])) == 5:
            # Check if the number shares exactly one digit in common in the same position as the number.
            for j in range(10):
                if List[i] != List[j]:
                    if len(set(str(List[i])) & set(str(List[j]))) == 1:
                        # Print the number.
                        print(List[i])
                        return
    print("No number is found.")

# Driver Code
Solution()