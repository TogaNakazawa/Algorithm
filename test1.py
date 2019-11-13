n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

def find_smaller_in_alist(index, b):
    for i in range(n):
        if a_list[i] <= b and a_list[index] <= b_list[i]:
            return i
    return -1
counter = 0

for i in range(n):
    if a_list[i] <= b_list[i]:
        pass
    elif counter == n-2:
        print("No")
        break
    else:
        counter += 1
        index = find_smaller_in_alist(i, b_list[i])
        if index == -1:
            print("No")
            break
        else:
            a_list[i], a_list[index] = a_list[index], a_list[i]
    if i == n-1:
        print("Yes")
