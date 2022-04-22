# For this problem, use the dictionary from the beginning of this chapter whose keys are month names and whose values are the number of days in the corresponding months.
# (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
# (b) Print out all of the keys in alphabetical order.
# (c) Print out all of the months with 31 days.
# (d) Print out the (key-value) pairs sorted by the number of days in each month
# (e) Modify the program from part (a) and the dictionary so that the user does not have to know how to spell the month name exactly. That is, all they have to do is spell the first three letters of the month name correctly.

def main():
    month_dict = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    while True:
        month = input("Enter month name: ")
        if month == "":
            break
        if month in month_dict:
            print(month_dict[month])
        else:
            print("Month not in dictionary")
    print("\n")
    for key in sorted(month_dict.keys()):
        print(key)
    print("\n")
    for key in sorted(month_dict.keys()):
        if month_dict[key] == 31:
            print(key)
    print("\n")
    for key in sorted(month_dict.keys()):
        print(key, month_dict[key])

main()