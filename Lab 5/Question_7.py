#! /bin/python3
# Write a function in Python which accepts a string and returns number of vowels present in it.

def count_vowels(s):
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for str in s:
        if str in vowel:
            count += 1
    return count

# Driver code
s = input("Enter a string: ")
print("The number of vowels in the string is: ", count_vowels(s))