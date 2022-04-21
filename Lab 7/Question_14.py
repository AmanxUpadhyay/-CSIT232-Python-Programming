# Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.

PalindromicNumbers = [x for x in range(100, 1000) if str(x) == str(x)[::-1]]
print(PalindromicNumbers)