# Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47].

L = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

# Use a list comprehension to produce a list of the gaps between consecutive entries in L. 

L = [x - y for x, y in zip(L[1:], L)]
print(L)

# Then find the maximum gap size and the percentage of gaps that have size 2.

MaximumGaplist = [x for x in L if x > 2]
print(MaximumGaplist)