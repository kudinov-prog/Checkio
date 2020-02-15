"""
You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. 
Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
Here you can find some useful information about the 12-hour format.
"""

def time_converter(time):
    new = time.split(" ")
    new_hm = new[0].split(":")
    
    if new[1] == "a.m." and int(new_hm[0]) == 12:
        return ("00" + ":" + new_hm[1])
        
    elif new[1] == "p.m." and int(new_hm[0]) == 12:
        return (new_hm[0] + ":" + new_hm[1])

    
    elif new[1] == "a.m." and int(new_hm[0]) <= 9:
        return ("0" + new_hm[0] + ":" + new_hm[1])
        
    elif new[1] == "a.m." and int(new_hm[0]) >= 9:
        return (new_hm[0] + ":" + new_hm[1])
    
    elif new[1] == "p.m." and int(new_hm[0]) <= 11:
        return (str(int(new_hm[0]) + 12) + ":" + new_hm[1])

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")