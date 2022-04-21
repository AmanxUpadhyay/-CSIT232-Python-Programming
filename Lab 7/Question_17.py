# Write a program that finds the average of all of the entries in a 4  4 list of integers.

List = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Average = sum(sum(List, []))/len(List)
print(Average)