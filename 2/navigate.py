def move(position, direction, step):
    print(position)
    horizontal = position[0]
    depth = position[1]
    if direction == "forward":
        new_position = (horizontal + step, depth)
    elif direction == "down":
        new_position = (horizontal, depth + step)
    else:
        new_position = (horizontal, depth - step)
    return(new_position)

def move_w_aim(position, direction, step):
    print(position)
    horizontal = position[0]
    depth = position[1]
    aim = position[2]
    if direction == "forward":
        new_position = (horizontal + step, depth + aim * step, aim)
    elif direction == "down":
        new_position = (horizontal, depth, aim + step)
    else:
        new_position = (horizontal, depth, aim - step)
    return(new_position)

directions = open("directions.txt", "r")
position = (0, 0)
for line in directions:
    direction, step = line.rstrip().split(" ")
    new_position = move(position, direction, int(step))
    position = new_position
print(position[0] * position[1])

directions = open("directions.txt", "r")
position_aim = (0, 0, 0)
for line in directions:
    direction, step = line.rstrip().split(" ")
    new_position = move_w_aim(position_aim, direction, int(step))
    position_aim = new_position
print(position_aim[0] * position_aim[1])
