# Suppose you are given the following list of strings:
# L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
# Patterns like this show up in many places, including DNA sequencing. The user has a string of their own with only some letters filled in and the rest as asterisks. An example is a**a****. The user would like to know which of the strings in the list fit with their pattern.
# In the example just given, the matching strings are the first and fourth. One way to solve this problem is to create a dictionary whose keys are the indices in the user’s string of the non-asterisk characters and whose values are those characters. Write a program implementing this approach (or some other approach) to find the strings that match a user-entered string.

def main():
    L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
    user_string = input("Enter string: ")
    user_string_dict = {}
    for i in range(len(user_string)):
        if user_string[i] != "*":
            user_string_dict[i] = user_string[i]
    print(user_string_dict)
    for string in L:
        string_dict = {}
        for i in range(len(string)):
            if string[i] != "*":
                string_dict[i] = string[i]
        print(string_dict)
        if user_string_dict == string_dict:
            print(string)

main()