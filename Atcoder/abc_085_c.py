n,y = map(int,input().split())
y //= 1000
temp = y//10
if temp > n:
    print("-1 -1 -1")
    quit()
for i in range(temp+1):
    zandaka = y - i * 10
    maisuu = n - i
    for k in range(maisuu+1):
        if k * 5 + maisuu - k == zandaka:
            print(str(i) + " " + str(k) + " " + str(maisuu-k))
            quit()

print("-1 -1 -1")
quit()
