length = int(input())
list = list(input())

counter = 0

for k in range(length-1):
    try:
        while True:
            if list[k] != list[k+1]:
                break
            list.pop(k+1)
    except:
        break


print(len(list))
