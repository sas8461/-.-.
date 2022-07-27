a = int(input())

def obr():
    b = 10**(len(str(a))-1)
    for i in range(len(str(a)), 0, -1):
        if i == 1:
            print(a % 10)
        else:
            print((a // b) % 10)
        b = b // 10
obr()