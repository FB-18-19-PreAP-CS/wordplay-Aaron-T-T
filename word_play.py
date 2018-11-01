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
    word = input('Say a word: ')
    print(word)

if __name__ == "__main__":
    avoids()