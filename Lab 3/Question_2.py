#
#  * Author: Aman Upadhyay
#  * Date: 02/03/2022
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# ! Write a program which accepts the user's first and last name and print them in reverse order with a space between them.
def NameChange(Fname, Lname):
    FullName = Fname + " " + Lname
    Res = ""
    for i in FullName:
        Res = i + Res
    print(Res)

# Driver Code
Fname = input("Enter your first name: ")
Lname = input("Enter your last name: ")
NameChange(Fname, Lname)