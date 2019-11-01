n = int(input())
list = list(map(int, input().split()))
list.sort()
list2 = [list[0]]
for i in range(1,n):
    list2.append(list[i] * 2 ** (i-1))

print(sum(list2) / 2 ** (n-1))
