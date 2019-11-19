n,m = map(int,input().split())
li = [list(map(int,input().split())) for i in range(m)]
odd_even = list( map(int,input().split()))
counter = 0
for i in range(2**n):
    switches = ["off"] * n
    num1 = 0
    for j in range(n):
        if (i>>j)&1:
            switches[n-j-1] = "on"
    for i in range(m):
        # numは条件に当てはまる電球の点灯数
        num = 0
        for k in range(1,len(li[i])):
            if switches[li[i][k]-1] == "on":
                num += 1
        if num % 2 == odd_even[i]:
            num1 += 1
            continue
        else:
            break
    if num1 == m:
        counter += 1
print(counter)
