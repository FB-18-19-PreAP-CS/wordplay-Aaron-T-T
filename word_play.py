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
    for i in range(0,len(letters)+1):
        if letters[i] not in word:
            return False
        else:
            return True
def words_uses_only():
    a = input('Put letters that you only want in the words: ')
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if uses_only(word,a):
                    count += 1
    print(count)
if __name__ == "__main__":
    words_uses_only()