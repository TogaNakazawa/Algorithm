n,k = map(int,input().split())
import numpy as np
food_costs = np.array(list(map(int,input().split())))
complexites = np.array(list(map(int,input().split())))

while True:
    times = food_costs * complexites
    if k > 0:
        food_costs[np.argmax(times)] -= 1
        k -= 1
    if k == 0:
        break
    if sum(food_costs) == 0:
        break
print(sum(food_costs))
