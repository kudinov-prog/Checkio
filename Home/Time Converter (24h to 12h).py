"""
You prefer a good old 12-hour time format. But the modern world we live in would rather 
use the 24-hour format and you see it everywhere. Your task is to convert the time 
from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
"""

def time_converter(input):
    time_split  = input.split(":")
    if int(time_split[0]) > 12:
        new_hour = int(time_split[0]) - 12
        return str(new_hour) + ":" + str(time_split[1]) + " p.m."
    elif 0 < int(time_split[0]) < 12:
        new_hour = int(time_split[0])
        return str(new_hour) + ":" + str(time_split[1]) + " a.m."
    elif int(time_split[0]) == 12:
        new_hour = int(time_split[0])
        return str(new_hour) + ":" + str(time_split[1]) + " p.m."
    elif int(time_split[0]) == 00:
        new_hour = int(time_split[0]) + 12
        return str(new_hour) + ":" + str(time_split[1]) + " a.m."

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")