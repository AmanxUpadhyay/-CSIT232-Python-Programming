# Let L be a list of strings. Write list comprehensions that create new lists from L for each of the following.
# (a) A list that consists of the strings of s with their first characters removed
# (b) A list of the lengths of the strings of s
# (c) A list that consists of only those strings of s that are at least three characters long

def RemoveSFromStart(s):
    return s[1:]

def AListOfStrings(L):
    return [RemoveSFromStart(s) for s in L]

def ListOnlyStringsLongerThanThree(L):
    return [s for s in L if len(s) > 3]

# Driver code
L = ["abc", "xyz", "aba", "1221"]
print(AListOfStrings(L))
print(ListOnlyStringsLongerThanThree(L))