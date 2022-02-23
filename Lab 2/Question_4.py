#
#  * Author: Aman Upadhyay
#  * Date: 23/02/2022
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to generate first N natural numbers.
def NaturalNumber(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

# Driver code
Number = int(input("Enter a number: "))
NaturalNumber(Number)