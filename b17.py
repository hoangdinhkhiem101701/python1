import math
def snt(a):
    if(a <= 1):
        return False
    else:
        for i in range(2, int(math.sqrt(a))+1):
            if(a % i == 0):
                return False
    return True

a, b = map(int, input().split())
for i in range (a, b+1):
    if(snt(i)):
        print(i, end = " ")