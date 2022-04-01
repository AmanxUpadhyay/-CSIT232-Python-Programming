# Write a program that asks the user for an integer and creates a list that consists of the factors of that integer.

# Function to find the factors of a number
def factors(num):
    factors_list = []
    for i in range(1, num+1):
        if num % i == 0:
            factors_list.append(i)
    return factors_list

# Driver Code
num = int(input("Enter an integer: "))
print("The factors of", num, "are: ", factors(num))