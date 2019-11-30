n = int(input())
list = list(map(int, input().split()))

dict = {}
count = 1

for i in list:
    dict[i]= count
    count += 1
for i in range(1, n+1):
    print(dict[i], end = " ")
