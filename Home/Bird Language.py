"""
You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). 
The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. 
You should translate this phrase from the bird language to something more understandable.
"""

VOWELS = "aeiouy"

def translate(phrase):
    human_phrase = [] 
    i = 0 
    while i < len(phrase):                   
        human_phrase.append(phrase[i]) 
        if phrase[i] in VOWELS: 
            i += 3 
        elif phrase[i] == ' ': 
            i += 1 
        else: 
            i += 2 
    return ''.join(human_phrase)
    

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")