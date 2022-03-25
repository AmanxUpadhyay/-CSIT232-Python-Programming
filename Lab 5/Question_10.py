#! /bin/python3
# Implement a python script for factorial of number by using recursive function.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Driver code
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))