n,k,q = map(int, input().split())
correct_answers = [int(input()) for i in range(q)]
points = [k-q for i in range(n)]
for i in range(q):
    points[correct_answers[i]-1] += 1

for point in points:
    if point < 1:
        print("No")
    else:
        print("Yes")
