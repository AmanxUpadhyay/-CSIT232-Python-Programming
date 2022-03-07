#
#  * Author: Aman Upadhyay
#  * Date: 7/03/2022
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# TODO
# * Ask the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed.
UserProvidedString = []
UpdatedString = []
ListSize = int(input("\nEnter the size of the list: "))
for i in range(ListSize):
    UserProvidedString.append(input("Enter the string: "))
    UpdatedString.append(UserProvidedString[i][1:])
print("\nOriginal List: ", UserProvidedString)
print("\nUpdated List: ", UpdatedString)
