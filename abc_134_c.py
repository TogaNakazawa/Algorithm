n = int(input())
import copy
list = []
for i in range(n):
    k = int(input())
    list.append(k)
list1 = copy.deepcopy(list)
first = max(list1)
list1.remove(first)
second = max(list1)
for li in list:
    if li == first:
        print(second)
    else:
        print(first)
