x = int(input())
y = x // 111
if x % 111 == 0:
    print(round(y * 111))
else:
    print(round((y+1)*111))
