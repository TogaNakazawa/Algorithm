n = int(input())
list = list(map(int, input().split()))

if n > 1:
    for i in reversed(range(n-1)) :
        if list[i+1] - list[i] < - 1:
            print("No")
            break
        elif  list[i+1] - list[i] == - 1:
            list[i] -= 1
        elif i == 0:
            print("Yes")
        else:
            continue
else:
    print("Yes")
