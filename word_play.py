import re



def at_least():
    with open("words.txt") as file:
        count_the = 0
        
        for line in file:
            for word in line.strip().split():
                count_the += 1
            if len(word) >= 20:
                print(word)
                
def has_no_e(word):
    if 'e' in word or 'E' in word:
        return False
    else:
        return True

def no_e():
    with open("words.txt") as file:
        count_the = 0
        count_th = 0
        for line in file:
            for word in line.strip().split():
                count_th += 1
                if has_no_e(word):
                    count_the += 1
        a = ((count_the / count_th) * 100) // 1
        b = int(a)
        print("{:2}%".format(b))
def avoids(word,letters):
    '''
    >>> avoids('abcde','a')
    False
    
    >>> avoids('bfge','c')
    True
    
    >>> avoids('abced','aere')
    False
    '''
    for i in range(0,len(letters)):
        if letters[i] in word:
            return False
    else:
        return True
def avoids_count():
    a = input('Put letters that you don\'t want in the words: ')
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if avoids(word,a):
                    count += 1
    print(count)
    
def uses_only(word,letters):
    '''
    
    >>> uses_only('false','flsae')
    True
    
    >>> uses_only('aabe','ab')
    False
    '''
    a = 0
    for i in range(0,len(word)):
        if word[i] not in letters:
            a = 3
            break 
        if word[i] in letters:
            a = 1
            
    if a == 3:
        return False
    if a == 1:
        return True
def words_with_only():
    a = input('Put letters that you only want in the words: ')
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if uses_only(word,a):
                    count += 1
                    print(word)
                    
def uses_all(word,letters):
    '''

    >>> uses_all('word','dorw')
    True
    >>> uses_all('word','words')
    False
    
    >>> uses_all('school','aglm')
    False

    >>> uses_all('words','word')
    True
    '''
    a = 0
    for i in range(0,len(word)):
        if word[i] in letters:
            a += 1
        elif word[i] not in letters:
            a += 0
    if a < len(letters):
        return False
    if a >= len(letters):
        return True


def how_many_uses_all():
    a = input('Put letters that you only want in the words: ')
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if uses_all(word,a):
                    count += 1
        print(count)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    how_many_uses_all()