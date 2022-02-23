# Author: Aman Upadhyay

# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?

def AlarmClock(hours):
    Time = 14
    Format = 24
    Result = (hours % Format) + Time

    if(Result > 12):
        Result = Result - 12
        print("The alarm will go off at", Result, ":00 PM")
    else:
        print("The alarm will go off at", Result, ":00 AM")


# Driver Code
AlarmClock(int(input("Enter hours: ")))