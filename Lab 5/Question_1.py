#! /bin/python3
# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Driver code
a, b, c = input("Enter three numbers: ").split()
print(max_of_three(int(a), int(b), int(c)))