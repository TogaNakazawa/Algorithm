n = int(input())
li = list(map(int,input().split()))
if n ==2:
    print(max(li))
else:
    li.sort()
    a = li.pop(0)
    def gcd(x, y):
        while y > 0:
            x, y = y, x%y
        return x
    ans = li[0]
    print(li)
    for i in range(1,n-1):
        ans = gcd(ans, li[i])
    li.insert(0,a)
    li.pop(1)
    ans1 = li[0]
    print(li)
    for i in range(1, n-1):
        ans1 = gcd(ans1, li[i])
    print(max(ans,ans1))
