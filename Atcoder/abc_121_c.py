n,m = map(int, input().split())
li = [list(map(int, input().split())) for i in range(n)]
li.sort(key=lambda x:x[0])
ans = 0

while True:
    if m == 0:
        print(ans)
        quit()
    if li[0][1] == 0:
        li.pop(0)
    ans += li[0][0]
    li[0][1] -= 1
    m -= 1
