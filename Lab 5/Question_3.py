#! /bin/python3
# Define a function which generates Fibonacci series up to n numbers.

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Driver code
n = int(input("Enter a number: "))
fibonacci(n)