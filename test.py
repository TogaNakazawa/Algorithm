n = int(input())
list = []
differences = []
for i in range(n):
    a,b = map(int,input().split())
    list.append([a,b])
    differences.append(b-a+1)
if max(differences) != min(differences):
    print(max(differences) + min(differences))133_c
