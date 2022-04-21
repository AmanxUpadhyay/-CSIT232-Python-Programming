# Write a program that creates a 5  5 list consisting of zeroes and ones. Your program should then pick a random location in the list that contains a zero and change it to a one. 

# If all the entries are one, the program should say so. [Hint: one way to do this is to create a new list whose items are the coordinates of all the ones in the list and use the choice method to randomly select one. Use a two-element list to represent a set of coordinates.]

import random

# Function to Make 5*5 List of 0s and 1s randomly
def MakeList():
    MemoryGame = []
    for i in range(5):
        MemoryGame.append([])
        for j in range(5):
            MemoryGame[i].append(random.choice([0, 1]))
    return MemoryGame

# Function to pick random location in list and check if it is 0 and change it to 1.
def ChangeList(MemoryGame):
    # Pick random location in list
    i = random.randint(0, 4)
    j = random.randint(0, 4)
    # Check if it is 0 and change it to 1.
    if MemoryGame[i][j] == 0:
        MemoryGame[i][j] = 1
    else:
        print("All the entries are one.")

# Function to check if all the entries are one.
def CheckList(MemoryGame):
    # Check if all the entries are one.
    for i in range(5):
        for j in range(5):
            if MemoryGame[i][j] == 0:
                return False
    return True

# Driver Code
MemoryGame = MakeList()
print("Original List:")
for i in range(5):
    for j in range(5):
        print(MemoryGame[i][j], end = " ")
    print()

choice = 0
while choice != -1:
    # Menu to choose 1. Change List 2. Check List 3. Exit
    print("\nMenu:")
    print("1. Change List")
    print("2. Check List")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ChangeList(MemoryGame)
    elif choice == 2:
        if CheckList(MemoryGame):
            print("All the entries are one.")
        else:
            print("There are still some entries that are not one.")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

# Print the list
    print("\nList:")
    for i in range(5):
        for j in range(5):
            print(MemoryGame[i][j], end = " ")
        print()