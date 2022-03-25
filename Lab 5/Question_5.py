#! /bin/python3
# Write a function in Python to double the odd numbers and half the even numbers present in the list (take the list as function parameter).

def double_odd_numbers(n):
    for i in range(len(n)):
        if n[i] % 2 != 0:
            n[i] = n[i] * 2
    return n

# Driver code
List = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    List.append(int(input("Enter the element: ")))
print("The doubled list is: ", double_odd_numbers(List))