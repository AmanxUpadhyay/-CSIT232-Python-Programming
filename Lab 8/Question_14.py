# The following problem is from Chapter 6. Try it again, this time using a dictionary whose
# keys are the names of the time zones and whose values are offsets from the Eastern time
# zone.
# Write a program that converts a time from one time zone to another. The user enters the time
# in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters
# is that of the original time and the second is the desired time zone. The possible time zones
# are Eastern, Central, Mountain, or Pacific.
# Time: 11:48pm
# Starting zone: Pacific
# Ending zone: Eastern
# 2:48am

def main():
    time_dict = {'Eastern':-5, 'Central':-6, 'Mountain':-7, 'Pacific':-8}
    time = input("Enter time: ")
    starting_zone = input("Enter starting zone: ")
    ending_zone = input("Enter ending zone: ")
    starting_time = time.split(" ")
    starting_time_hour = int(starting_time[0])
    starting_time_minute = int(starting_time[1][:-2])
    starting_time_ampm = starting_time[1][-2:]
    if starting_time_ampm == "pm":
        starting_time_hour += 12
    starting_time_minute += time_dict[starting_zone]
    if starting_time_minute < 0:
        starting_time_minute += 60
        starting_time_hour -= 1
    if starting_time_minute > 59:
        starting_time_minute -= 60
        starting_time_hour += 1
    if starting_time_hour > 23:
        starting_time_hour -= 24
    ending_time_hour = starting_time_hour + time_dict[ending_zone]
    ending_time_minute = starting_time_minute
    if ending_time_minute < 0:
        ending_time_minute += 60
        ending_time_hour -= 1
    if ending_time_minute > 59:
        ending_time_minute -= 60
        ending_time_hour += 1
    if ending_time_hour > 23:
        ending_time_hour -= 24
    ending_time_ampm = "am"
    if ending_time_hour > 12:
        ending_time_hour -= 12
        ending_time_ampm = "pm"
    print(ending_time_hour, ending_time_minute, ending_time_ampm)

main()