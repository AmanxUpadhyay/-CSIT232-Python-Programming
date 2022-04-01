# Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].

# Function to add two lists
def add_lists(L, M):
    N = []
    for i in range(len(L)):
        N.append(L[i] + M[i])
    return N

# Driver Code
L = [], M = []
print("Enter the elements of the first list: ")
for i in range(3):
    L.append(int(input()))
print("Enter the elements of the second list: ")
for i in range(3):
    M.append(int(input()))
print("The sum of the two lists is: ", add_lists(L, M))