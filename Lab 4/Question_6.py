#
#  * Author: Aman Upadhyay
#  * Date: 7/03/2022
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# TODO
# *  A list consisting of the integers 0 through 49
MadeList = []
for i in range(0, 50):
    MadeList.append(i)
print("\nList with Integers 0 to 49: ", MadeList)

# * A list containing the squares of the integers 0 through 49
SquaredList = []
for i in range(0, 50):
    SquaredList.append(i**2)
print("\nList with Squares of Integers 0 to 49: ", SquaredList)

# * The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
AlphabatesList = []
for i in range(0, 26):
    AlphabatesList.append(chr(i + 97)*i)
print("\nList with 26 Alphabates: ", AlphabatesList)