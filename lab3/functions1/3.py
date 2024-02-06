#2c + 4r = 94
#2c + 2r = 70
#r = 12
#c = 35 - 12 = 23

def fun(h, l):
    r = (l - 2*h)//2
    c = h - r
    print("Num of rabbits =", r, "Num of chickens", c)
    # (c + r) = h
    # 2c + 2r = 2h
    # 2c = 2h - 2r
    # (2*c + 4*r) = l
    # 2c = l - 4r
    # 2h - 2r = l - 4r
    # 2r = l - 2h
    # r = (l-2h)/3


fun(35, 94)