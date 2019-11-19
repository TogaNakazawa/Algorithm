n,m = map(int,input().split())
l,r = map(int,input().split())
counter = 0
for i in range(m-1):
    l1,r1 = map(int,input().split())
    if l < l1:
        l = l1
    if r > r1:
        r = r1
if r < l:
    print(0)
else:
    print(r-l+1)
