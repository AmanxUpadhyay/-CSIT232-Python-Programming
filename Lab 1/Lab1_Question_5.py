# Author: Aman Upadhyay

# Write a python program to compute distance between two points taking input from the user (use Pythagorean Theorem, sqrt( ) or a**.5 to find the square root)

def PythagoreanTheorem(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Driver Code
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
print("Distance between ({}, {}) and ({}, {}) is {}".format(x1, y1, x2, y2, PythagoreanTheorem(x1, y1, x2, y2)))