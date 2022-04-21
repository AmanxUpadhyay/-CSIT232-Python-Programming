# Write a program that creates and prints an 8 x 8 list whose entries alternate between 1 and 2 in a checkerboard pattern, starting with 1 in the upper left corner.

UserInput = int(input("Enter the number of rows and columns you want in your list: "))
List = [[1 if i % 2 == 0 and j % 2 == 0 else 2 if i % 2 == 1 and j % 2 == 1 else 0 for j in range(UserInput)] for i in range(UserInput)]

for i in range(UserInput):
    for j in range(UserInput):
        print(List[i][j], end = " ")
    print()