number_of_space, number_of_robots, number_of_blocks = map(int, input().split())
goals = list(map(int, input().split()))
blocks = []
robots = []
directions = []
new_directions = []
new_coordinates = []
right_coordinates = []
left_coordinates = []
up_coordinates = []
down_coordinates = []

for i in range(number_of_robots):
    li = input().split()
    robots.append([int(li[0]),int(li[1])])
    directions.append(li[2])
for i in range(number_of_blocks):
    li = list(map(int, input().split()))
    blocks.append(li)

def block_surrounding_coordinates(y, x):
    if x == 0:
        left_coordinate = [y, 39]
    else:
        left_coordinate = [y, x - 1]
    if x == 39:
        right_coordinate = [y, 0]
    else:
        right_coordinate = [y, x + 1]
    if y == 0:
        up_coordinate = [39, x]
    else:
        up_coordinate = [y-1, x]
    if y == 39:
        down_coordinate = [0, x]
    else:
        down_coordinate = [y + 1, x]
    return right_coordinate, left_coordinate, up_coordinate, down_coordinate


for block in blocks:
    right_coordinate, left_coordinate, up_coordinate, down_coordinate = block_surrounding_coordinates(block[0], block[1])

    right_coordinates.append(right_coordinate)
    left_coordinates.append(left_coordinate)
    up_coordinates.append(up_coordinate)
    down_coordinates.append(down_coordinate)

right_goals, left_goals, up_goals, down_goals = block_surrounding_coordinates(goals[0], goals[1])

def add_directions_toward_goals(goals, blocks):
    for x in range(goals[1]):
        # 第2象限
        for y in range(goals[0] - 1):
            if [y,x] not in blocks and [y,x] not in new_coordinates:
                if [y,x] not in up_coordinates:
                    new_coordinates.append([y,x])
                    new_directions.append("D")
                else:
                    if [y,x] not in left_coordinates:
                        new_coordinates.append([y,x])
                        new_directions.append("R")
                    else:
                        new_coordinates.append([y,x])
                        new_directions.append("L")
        # 第3象限
        for y in range(goals[0] + 1, 40):
            if [y,x] not in blocks and [y,x] not in new_coordinates:
                if [y,x] not in down_coordinates:
                    new_coordinates.append([y,x])
                    new_directions.append("U")
                else:
                    if [y,x] not in left_coordinates:
                        new_coordinates.append([y,x])
                        new_directions.append("R")
                    else:
                        new_coordinates.append([y,x])
                        new_directions.append("L")
    for x in range(goals[1] + 1, 40):
        # 第1象限
        for y in range(goals[0] - 1):
            if [y,x] not in blocks and [y,x] not in new_coordinates:
                if [y,x] not in up_coordinates:
                    new_coordinates.append([y,x])
                    new_directions.append("D")
                else:
                    if [y,x] not in right_coordinates:
                        new_coordinates.append([y,x])
                        new_directions.append("L")
                    else:
                        new_coordinates.append([y,x])
                        new_directions.append("R")
        # 第4象限
        for y in range(goals[0] + 1, 40):
            if [y,x] not in blocks and [y,x] not in new_coordinates:
                if [y,x] not in down_coordinates:
                    new_coordinates.append([y,x])
                    new_directions.append("U")
                else:
                    if [y,x] not in right_coordinates:
                        new_coordinates.append([y,x])
                        new_directions.append("L")
                    else:
                        new_coordinates.append([y,x])
                        new_directions.append("R")
    return new_directions, new_coordinates

new_directions, new_coordinates = add_directions_toward_goals(goals, blocks)


def get_duplicate_list(seq):
    seen = []
    return [x for x in seq if not seen.append(x) and seen.count(x) == 2]

if left_goals not in blocks:
    if [left_goals[0], left_goals[1]-1] not in blocks:
        if [left_goals[0], left_goals[1]-1] not in new_coordinates:
            new_coordinates.append([left_goals[0], left_goals[1]-1])
            new_directions.append("U")
        else:
            new_directions[new_coordinates.index([left_goals[0], left_goals[1]-1])] = "U"
    if [left_goals[0]-1, left_goals[1]-1] not in blocks:
        if [left_goals[0]-1, left_goals[1]-1] not in new_coordinates:
            new_coordinates.append([left_goals[0]-1, left_goals[1]-1])
            new_directions.append("R")
        else:
            new_directions[new_coordinates.index([left_goals[0]-1, left_goals[1]-1])] = "R"
    if [left_goals[0]-1, left_goals[1]] not in blocks:
        if [left_goals[0]-1, left_goals[1]] not in new_coordinates:
            new_coordinates.append([left_goals[0]-1, left_goals[1]])
            new_directions.append("R")
        else:
            new_directions[new_coordinates.index([left_goals[0]-1, left_goals[1]])] = "R"
if right_goals not in blocks:
    if [right_goals[0], right_goals[1]+1] not in blocks:
        if [right_goals[0], right_goals[1]+1] not in new_coordinates:
            new_coordinates.append([right_goals[0], right_goals[1]+1])
            new_directions.append("U")
        else:
            new_directions[new_coordinates.index([left_goals[0], left_goals[1]+1])] = "U"
    if [right_goals[0]-1, right_goals[1]+1] not in blocks:
        if [right_goals[0]-1, right_goals[1]+1] not in new_coordinates:
            new_coordinates.append([right_goals[0]-1, right_goals[1]+1])
            new_directions.append("L")
        else:
            new_directions[new_coordinates.index([left_goals[0]-1, left_goals[1]+1])] = "L"
    if [right_goals[0]-1, right_goals[1]] not in blocks:
        if [right_goals[0]-1, right_goals[1]] not in new_coordinates:
            new_coordinates.append([right_goals[0]-1, right_goals[1]])
            new_coordinates.append("L")
        else:
            new_directions[new_coordinates.index([left_goals[0]-1, left_goals[1]])] = "L"

test = new_coordinates + blocks
tests = get_duplicate_list(test)))
for i in tests:
    k = new_coordinates.index(i)
    new_directions.pop(k)
    new_coordinates.pop(k)



print(len(new_directions))
for i in range(len(new_directions)):
    print(str(new_coordinates[i][0]) + " " + str(new_coordinates[i][1]) + " " + new_directions[i])
