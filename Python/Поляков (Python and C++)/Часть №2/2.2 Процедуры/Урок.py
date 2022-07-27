def printLine10(n):
    print("-" * n)

def triangle0(n):
    for i in range(1, n+1):
        print('0'*i)

i = 15
def ShowGlobal():
    global i
    i = 5
    print(i)