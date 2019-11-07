n = int(input())
list = list(map(int, input().split()))
list1 = sorted(list)
median_candidate1, median_candidate2 = list1[n//2-1], list1[n//2]
for i in list:
    if i <= median_candidate1:
        print(median_candidate2)
    else:
        print(median_candidate1)
