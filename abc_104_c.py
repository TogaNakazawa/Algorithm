n,g = map(int, input().split())
standard = []
bonus = []
num_of_problems = []
for i in range(n):
    a,b = map(int, input().split())
    standard.append(a * (i+1) * 100)
    bonus.append(b)
    num_of_problems.append(a)
points_after_completion = []
min_num = 10 * 100
for i in range(2**n):
    point = 0
    num = 0
    li = list(range(n))
    for j in range(n):
        if (i >> j) & 1:
            point += standard[n-j-1] + bonus[n-j-1]
            num += num_of_problems[n-j-1]
            li.remove(n-j-1)
    counter = 0
    if li != []:
        while point < g and counter <= num_of_problems[li[-1]]:
            point += 100 * (li[-1]+1)
            num += 1
            counter += 1
    if num < min_num and point >= g:
        min_num = num
print(min_num)
