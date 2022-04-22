# (a) Write a program that converts Roman numerals into ordinary numbers. Here are the
# conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things
# like IV being 4 and XL being 40.
# (b) Write a program that converts ordinary numbers into Roman numerals

def RomanNumberToOrdinaryNumber(roman_number):
    roman_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    ordinary_number = 0
    for i in range(len(roman_number)):
        if i == 0:
            ordinary_number += roman_dict[roman_number[i]]
        elif roman_dict[roman_number[i]] > roman_dict[roman_number[i-1]]:
            ordinary_number += roman_dict[roman_number[i]] - 2 * roman_dict[roman_number[i-1]]
        else:
            ordinary_number += roman_dict[roman_number[i]]
    return ordinary_number

def OrdinaryNumberToRomanNumber(ordinary_number):
    roman_dict = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
    roman_number = ''
    for i in roman_dict:
        while ordinary_number >= i:
            roman_number += roman_dict[i]
            ordinary_number -= i
    return roman_number

# Driver Code
print(RomanNumberToOrdinaryNumber('MMMCMXCIX'))
print(OrdinaryNumberToRomanNumber(3999))