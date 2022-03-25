#! /bin/python3
# Define a function that checks whether the given number is Armstrong

def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False

# Driver code
n = int(input("Enter a number: "))
if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")