# Write a program that checks to see if a 4  4 list is a magic square. In a magic square, every row, column, and the two diagonals add up to the same value.

def MagicSquare(List):
    Sum = sum(sum(List, []))
    for i in range(4):
        if sum(List[i]) != Sum:
            return False
    for i in range(4):
        if sum([List[j][i] for j in range(4)]) != Sum:
            return False
    if sum([List[i][i] for i in range(4)]) != Sum:
        return False
    if sum([List[i][3-i] for i in range(4)]) != Sum:
        return False
    return True

# Driver Code
# Take List 4*4 values from User
List = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    for j in range(4):
        List[i][j] = int(input("Enter the value for List[{}][{}]: ".format(i, j)))

if MagicSquare(List):
    print("This is a Magic Square")
else:
    print("This is not a Magic Square")