n = int(input())
li = []
for i in range(n):
    a,b = map(int, input().split())
    li.append([a,b])
import math
def length(cor1,cor2):
    l = math.sqrt((cor2[0] - cor1[0])**2 + (cor2[1] - cor1[1])**2)
    return l

max = 0
for i in range(n-1):
    for k in range(i+1,n):
        if max < length(li[i], li[k]):
            max = length(li[i], li[k])
print(max)
