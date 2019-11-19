n = int(input())
list = list(map(int, input().split()))
list.sort()
import bisect
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        index = bisect.bisect_left(list, list[i]+list[j])
        ans += index - j -1
print(ans)
