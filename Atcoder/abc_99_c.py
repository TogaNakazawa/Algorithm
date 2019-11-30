n = int(input())
min = n
count = 0
def acceptable_mutiples(n,num):
    li = []
    import copy
    default = copy.deepcopy(num)
    while n // num > 0:
        li.append(num)
        num *= default
    return li

sixes = acceptable_mutiples(n,6)
nines = acceptable_mutiples(n,9)
li = sixes + nines
li.sort()

import bisect
