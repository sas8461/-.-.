a = int(input())

def obr():
    b = 10
    for i in range(1, len(str(a))+ 1):
        if i == 1:
            print(a % b)
        elif i == len(str(a)):
            print(a // (b//10))
        else:
            print((a % b) // (b // 10))
        b = b * 10
obr()