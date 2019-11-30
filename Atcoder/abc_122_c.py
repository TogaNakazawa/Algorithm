n,q = map(int, input().split())
import bisect
str = list(input())
index = []
for i in range(n-1):
    if str[i] == "A" and str[i+1] == "C":
        index.append(i)
index.sort()
li = []
counter = 0
for i in range(q):
    s,t = map(int, input().split())
    head = bisect.bisect_left(index, s-1)
    tail = bisect.bisect_left(index, t-1)
    print(tail - head)
