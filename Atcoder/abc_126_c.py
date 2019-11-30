n,k = map(int,input().split())
win_rate = 0
if n >=k:
    win_rate += (n-k+1)/n
    for i in range(1,k):
        rate = 1
        while i < k:
            i *= 2
            rate *= 0.5
        win_rate += rate * (1/n)
    print(win_rate)
else:
    for i in range(1,n+1):
        rate = 1
        while i < k:
            i *= 2
            rate *= 0.5
        win_rate += rate * (1/n)
    print(win_rate)
