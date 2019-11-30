L,R = map(int, input().split())

def repeat_division(n):
    while True:
        if n < 2019:
            break
        n %= 2019
    return n

l = repeat_division(L)
r = repeat_division(R)

if R - L  >= 2019:
    print(0)
elif l > r:
    print(0)
else:
    min = 2019
    for k in range(l, r):
        for i in range(k+1,r+1):
            if min > repeat_division(k * i):
                min = repeat_division(k * i)
    print(min)
