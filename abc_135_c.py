n = int(input())
number_of_monsters =  list(map(int,input().split()))
feasible_beat =  list(map(int,input().split()))

start = sum(number_of_monsters)
for i in range(n):
    if number_of_monsters[i] < feasible_beat[i]:
        number_of_monsters[i+1] -= (feasible_beat[i] - number_of_monsters[i])
        number_of_monsters[i] = 0
        if number_of_monsters[i+1] < 0:
            number_of_monsters[i+1] = 0
    else:
        number_of_monsters[i] -= feasible_beat[i]
print(start-sum(number_of_monsters))
