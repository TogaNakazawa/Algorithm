n = int(input())
difficulties = list(map(int, input().split()))
difficulties.sort()
before_median = difficulties[int(n/2-1)]
after_median = difficulties[int(n/2)]

print(int(after_median - before_median))
