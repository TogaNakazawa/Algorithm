k,s = map(int,input().split())
counter = 0
for i in range(k+1):
    rest = s-i
    for n in range(rest+1):
        if rest - n <= k and n <= k:
            counter += 1
print(counter)
