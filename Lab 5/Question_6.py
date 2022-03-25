#! /bin/python3
# Write a function in Python which accepts a nested list and print all the values present at the main diagonal position in the form of a matrix

def print_diagonal(n):
    for i in range(len(n)):
        for j in range(len(n[i])):
            if i == j:
                print(n[i][j], end=" ")
    print()

# Driver code
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
List = []
for i in range(n):
    List.append([])
    for j in range(m):
        List[i].append(int(input("Enter the element: ")))
print_diagonal(List)
