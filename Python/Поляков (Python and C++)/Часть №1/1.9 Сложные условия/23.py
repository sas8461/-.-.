x, a, b = map(float, input().split())
if x >= a:
    if x <= b:
        print('В отрезке')
    else:
        print('Не в отрезке')
else:
    print('Не в отрезке')
if x >= a and x <= b:
    print('В отрезке')
else:
    print('Не в отрезке')