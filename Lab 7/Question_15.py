#  Use a list comprehension to create the list below, which consists of ones separated by increasingly many zeroes. The last two ones in the list should be separated by ten zeroes.

# Function to Print a list Pattern
# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

L = [j for i in range(11) for j in [1, *([0]*i)]]
print(L)