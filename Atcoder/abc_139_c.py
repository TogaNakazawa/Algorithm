n = int(input())
integers = list(map(int, input().split()))

max_moves = 0
moves = 0
for i in range(n-1):
    if integers[i] >= integers[i+1]:
        moves += 1
    else:
        moves = 0
    if max_moves < moves:
        max_moves = moves
print(max_moves)
