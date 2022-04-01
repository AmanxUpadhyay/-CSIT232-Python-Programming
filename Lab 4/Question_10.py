# Write a program that rotates the elements of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index

# Function to rotate the elements of a list
def rotate_list(List):
    temp = List[0]
    for i in range(len(List)-1):
        List[i] = List[i+1]
    List[len(List)-1] = temp
    return List

# Driver Code
List = []
print("Enter the elements of the list: ")
for i in range(5):
    List.append(int(input()))
print("The list after rotating is: ", rotate_list(List))