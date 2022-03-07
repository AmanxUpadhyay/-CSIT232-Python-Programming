#
#  * Author: Aman Upadhyay
#  * Date: 7/03/2022
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# TODO
# * Start with the List[8, 9, 10].
StartList = [8, 9, 10]
print("\nStart List: ", StartList)

# * Set the second entry (index 1) to 17
StartList[1] = 17
print("\nStart List: ", StartList)

# * Add 4, 5, and 6 to the end of the list
StartList.append(4)
StartList.append(5)
StartList.append(6)
print("\nStart List: ", StartList)

# * Remove the first entry from the list
StartList.pop(0)
print("\nStart List: ", StartList)

# * Sort the list
StartList.sort()
print("\nStart List: ", StartList)

# * Double the list
StartList = StartList * 2
print("\nStart List: ", StartList)

# * Insert 25 at index 3 The final list should equal
StartList.insert(3, 25)
print("\nStart List: ", StartList)
