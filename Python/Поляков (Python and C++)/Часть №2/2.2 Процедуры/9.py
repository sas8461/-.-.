def ramka(w, h):
    for i in range(1, h + 1):
        if i == 1:
            print("." * w)
        elif i == h:
            print("." * w)
        else:
            print(".", " " * (w - 4), ".")
ramka(6, 4)