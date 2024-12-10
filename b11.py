n = int(input())
s = 0
gt = 1
for i in range(1, n+1):
    gt *= i
    s += gt
print(s)