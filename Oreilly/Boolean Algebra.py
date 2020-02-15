"""
https://py.checkio.org/en/mission/boolean-algebra/
"""

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction":
        if x==0 and y==0:
            return 0
        elif x==1 and y==0:
            return 0
        elif x==0 and y ==1:
            return 0
        elif x==1 and y ==1:
            return 1
    elif operation == "disjunction":
        if x==0 and y==0:
            return 0
        elif x==1 and y==0:
            return 1
        elif x==0 and y ==1:
            return 1
        elif x==1 and y ==1:
            return 1
    elif operation == "implication":
        if x==0 and y==0:
            return 1
        elif x==1 and y==0:
            return 0
        elif x==0 and y ==1:
            return 1
        elif x==1 and y ==1:
            return 1
    elif operation == "exclusive":
        if x==0 and y==0:
            return 0
        elif x==1 and y==0:
            return 1
        elif x==0 and y ==1:
            return 1
        elif x==1 and y ==1:
            return 0
    elif operation == "equivalence":
        if x==0 and y==0:
            return 1
        elif x==1 and y==0:
            return 0
        elif x==0 and y ==1:
            return 0
        elif x==1 and y ==1:
            return 1
    
        
            
        
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')

"""
x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
-------------------------------------- """