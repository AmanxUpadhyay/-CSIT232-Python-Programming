# Using a for loop, create the list below, which consists of ones separated by increasingly many zeroes. The last two ones in the list should be separated by ten zeroes. [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

# Function to create the list
def create_list(num):
    num_list =[1]
    for i in range(num):
        num_list = num_list + (i * [0]) + [1]
    return num_list

# Driver Code
num = int(input("Enter the number of ones: "))
print("The list is: ", create_list(num))