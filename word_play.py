import re



def at_least():
    with open("words.txt") as file:
        count_the = 0
        
        for line in file:
            for word in line.strip().split():
                count_the += 1
            if len(word) >= 20:
                print(word)
def no_e():
    with open("words.txt") as file:
        count_the = 0
        count_th = 0
        for line in file:
            for word in line.strip().split():
                count_th += 1
                if 'e' not in word:
                    count_the += 1
        a = ((count_the / count_th) * 100) // 1
        b = int(a)
        print("{:2}%".format(b))
        
def avoids():
    a = ['a','e','b','c']
    
    word = input('Say a word: ')
    for i in range(0,len(word)):
        if a[i] in word:
            return False
        else:
            return True
def avoids_count():
    a = input('Put letters that you don\'t want in the words: ')
    b = list(a)
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if b[] not in word:
                    count += 1
if __name__ == "__main__":
    avoids_count()