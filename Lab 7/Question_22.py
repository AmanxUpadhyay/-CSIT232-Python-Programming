# The following is useful as part of a program to play Battleship. Suppose you have a 5*5 list that consists of zeroes and ones.
# Ask the user to enter a row and a column. If the entry in the list at that row and column is a one, the program should print Hit and otherwise it should print Miss.

def Battleship(List, Row, Column):
    if List[Row][Column] == 1:
        print("Hit")
    else:
        print("Miss")
    
# Driver Code

# Create a 5*5 list that consists of zeroes and ones randomly
import random
List = [[random.randint(0,1) for i in range(5)] for j in range(5)]

Row = int(input("Enter a row: "))
Col = int(input("Enter a column: "))

Battleship(List, Row, Col)