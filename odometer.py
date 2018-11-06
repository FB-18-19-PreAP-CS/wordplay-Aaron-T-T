def odometer():
    for i in range(100000):
        num = str(i)
        if num[2:] == num[5:1:-1]:
            num = int(i)
            num += 1
            num = str(i).zfill(6)
            if num[1:] == num[5:0:-1]:
                num = int(i)
                num += 2
                num = str(i).zfill(6)
                if num[0:] == num[5:0:-1]:
                    num = int(i)
                    num += 3
                    num = str(i).zfill(6)
    print(num)


if __name__ == "__main__":
    odometer()