"""
https://py.checkio.org/en/mission/cipher-map2/
"""

def recall_password(data, ciphered_password):
    summ_iter = [list(data)] 
    def rotatematrix(data): 
        newdata = []
        for i in range(len(data[0])):
            newrow = [data[j][i] for j in range(len(data))][::-1]
            newdata.append(''.join(newrow))   
        summ_iter.append(newdata)
   
    final_pass = []
    def split(data, ciphered_password):
        new_data = []
        new_password = []
        for i in data:
            for j in i:
                new_data.append(j)
        for f in ciphered_password:
            for k in f:
                new_password.append(k)
        for i in range(len(new_data)):
            if new_data[i] == 'X':
                final_pass.append(new_password[i])

    def main():
        i = 0
        while i <= 2:
            rotatematrix(summ_iter[i])
            i += 1
        z = 0
        while z < 4:
            split(summ_iter[z], ciphered_password)
            z += 1
        return ''.join(final_pass)
    
    return main()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'