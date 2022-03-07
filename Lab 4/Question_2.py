import random

# * Write a program that generates a list of 20 random numbers between 1 and 100.
RandomNumberList = []
for i in range(0, 20):
    RandomNumberList.append(random.randint(1, 100))

# * Print the List.
print("\nRandom Number List: ", RandomNumberList)

# * Print the average of the elements in the list.
sum = 0
for i in range(0, len(RandomNumberList)):
    sum = sum + RandomNumberList[i]
print("\nAverage of the elements in the list: ", sum / len(RandomNumberList))

# * Print the Largest and Smallest elements in the list.
RandomNumberList.sort()
print("\nLargest element in the list: ", RandomNumberList[-1])
print("\nSmallest element in the list: ", RandomNumberList[0])

# * Print the second largest and second smallest entries in the list
print("\nSecond largest element in the list: ", RandomNumberList[-2])
print("\nSecond smallest element in the list: ", RandomNumberList[1])

# * Print how many even numbers are in the list.
count = 0
for i in range(0, len(RandomNumberList)):
    if RandomNumberList[i] % 2 == 0:
        count = count + 1
print("\nNumber of even numbers in the list: ", count)
