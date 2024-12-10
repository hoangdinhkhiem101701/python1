def ucln(a, b):
    while(a*b != 0):
        if(a > b):
            a %= b
        else:
            b %= a
    return a + b

a, b = map(int, input().split())
print(ucln(a, b))