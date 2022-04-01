# Write a program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

# Function to remove repeated items from a list
def Solution(List):
    result = []
    for i in List:
        if i not in result:
            result.append(i)
    return result

# Driver Code
List = [1,1,2,3,4,3,0,0]
print("The list is: ", List)
print("The list after removing repeated items is: ", Solution(List))