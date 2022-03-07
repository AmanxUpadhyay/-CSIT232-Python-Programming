# TODO:
# * Take user input in Integer List.
IntegerList = []
ListSize = int(input("Enter the size of the list: "))
for i in range(0, ListSize):
    IntegerList.append(int(input("Element: ")))

# * Print the Total Number of Items in the List.
print("\nTotal Number of Items in the List: ", len(IntegerList))

# * Print the last item in the list.
print("\nLast Item in the List: ", IntegerList[-1])

# * Print the list in reverse order.
print("\nList in Reverse Order: ")
counter = len(IntegerList) - 1
while counter >= 0:
    print(IntegerList[counter])
    counter -= 1

# * Print Yes if the list contains a 5 and No otherwise.
print("\nChecking if the list contains a 5: ")
count = 0
for i in range(0, len(IntegerList)):
    if IntegerList[i] == 5:
        count += 1
if count > 0:
    print("Yes")
else:
    print("No")

# * Print the number of fives in the list.
print("\nNumber of fives in the list: ", count)

# * Remove the first and last items from the list, sort the remaining items, and print the result.
IntegerList.pop(0)
IntegerList.pop(-1)
IntegerList.sort()
print("\nSorted List: ", IntegerList)

# * Print how many integers in the list are less than 5.
print("\nNumber of Integers in the List less than 5: ")
for i in range(0, len(IntegerList)):
    if IntegerList[i] < 5:
        print(IntegerList[i])