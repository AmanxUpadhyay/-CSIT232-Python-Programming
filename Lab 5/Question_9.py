#! /bin/python3
# Implement a python script for Call-by-value and Call-by-reference

def call_by_value(a):
    a = a + 1
    print("Inside the function: ", a)

def call_by_reference(a):
    a = a + 1
    print("Inside the function: ", a)

# Driver code
a = 10
print("Before the function: ", a)
call_by_value(a)
print("After the function: ", a)
a = 10
print("Before the function: ", a)
call_by_reference(a)
print("After the function: ", a)