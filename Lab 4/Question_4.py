# TODO
# * Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10.
ContainList = []
ListSize = int(input("\nEnter the size of the list: "))
for i in range(ListSize):
    ContainList.append(int(input("Enter the number: ")))
    if(ContainList[i] > 10):
        ContainList[i] = 10
print("\nStart List: ", ContainList)