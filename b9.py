x, n = map(int, input().split())
s = 0
for i in range (n):
    s += x**i
print(s)