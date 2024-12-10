import math
def sohoanhao(a):
    tong = 0
    for i in range (1, int(math.sqrt(a)) + 1):
        tong += i
        if(i != a // i):
            tong += a // i
    if(tong - a == a):
        return True
    return False

a = int(input())
if(sohoanhao(a)):
    print(a, "la so hoan hao")
else:
    print(a, "khong la so hoan hao")