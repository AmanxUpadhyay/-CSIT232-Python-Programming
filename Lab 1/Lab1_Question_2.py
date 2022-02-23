# Author: Aman Upadhyay

# Write a python program for finding biggest number among 3 integers.

def BiggestNumber(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

# Driver Code
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("The biggest number is: ", BiggestNumber(num1, num2, num3))