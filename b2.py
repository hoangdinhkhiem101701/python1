a, b = map(int, input().split())
if(a > 0):
    print("x >", -b/a)
elif(a < 0):
    print("x <", -b/a)
else:
    if(b > 0):
        print("VSN")
    else:
        print("VN")