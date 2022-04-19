# Program to print the keys of the Dictionary and their values is an alphabetical order.

UserDictionary = {}
Element = 5
while Element != 0:
    UserKey = input("Enter a key: ")
    if UserKey == "":
        break
    UserValue = input("Enter a value: ")
    UserDictionary[UserKey] = UserValue
    Element -= 1

# Print the Dictionary and their values is an alphabetical order.
print("\nKey\t\tValue")
for i in sorted(UserDictionary):
    print(i, "\t\t", UserDictionary[i])