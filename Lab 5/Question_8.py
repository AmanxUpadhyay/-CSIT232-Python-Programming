#! /bin/python3
# Write a function in Python which accepts a string and returns the updated string where the uppercase alphabet will be replaced with lowercase and vice versa. also replace all the digits with # and all other charecters with %

def replacement(string):
    Result = ""
    for i in range(len(string)):
        if string[i].isupper():
            Result += string[i].lower()
        elif string[i].islower():
            Result += string[i].upper()
        elif string[i].isdigit():
            Result += '#'
        else:
            Result += '%'
    return Result

# Driver code
string  = input("Enter a string: ")
print(replacement(string))