from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
q = 0
w = 0
r = 0
stop = 0
while stop != 5:
    t = 15 * a + 17 * b + 21 * c
    if t == 185 and a != q and w != b and c != r:
        stop = stop + 1
        print("15 *", a, "+ 17 *", b, "+ 21 *", c, stop)
        q = a
        w = b
        r = c
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)