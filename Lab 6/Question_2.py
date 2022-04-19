
UserInput = input("Enter a string: ")
# Change String into Dictionary
Dict = {}
for i in UserInput:
    if i.isalpha():
        if i.lower() in Dict:
            Dict[i.lower()] += 1
        else:
            Dict[i.lower()] = 1
# Sort Dictionary
SortedDict = sorted(Dict.items())

# Print Dictionary
print("\nLetter\t\tCount")
for i in SortedDict:
    print(i[0], "\t\t", i[1])