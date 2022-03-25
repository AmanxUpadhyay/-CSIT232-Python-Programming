#! /bin/python3
# Write a program which makes use of function to display all such numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000.

def divisible_by_7_but_not_5(a, b):
    for i in range(a, b):
        if i % 7 == 0 and i % 5 != 0:
            print(i)

# Driver code
divisible_by_7_but_not_5(1000, 2000)