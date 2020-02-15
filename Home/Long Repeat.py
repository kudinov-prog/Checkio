"""
This mission is the first one of the series. Here you should find the length of the longest 
substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings 
with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.
"""

def long_repeat(line: str) -> int:
    count = 1
    i = 1
    dict = {}
    if line == "":
        return 0 
    elif len(line) == 1:
        return 1
        
    while i < len(line):
        a, b = line[i], line[i-1]
        if a == b:
            count += 1
            dict[i] = count
            i += 1
        else:
            dict[i] = 1
            i += 1
            count = 1
            
    return max(dict.values())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')