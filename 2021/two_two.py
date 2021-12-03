# declare stuff ahead of time -- force of habit
position = [0, 0]
aim = 0

with open('./input/2.txt', 'r') as instructions:
    for line in instructions:
        # Parsing nonsense
        ins = line.split(" ")
        index = 0 if ins[0] == "forward" else 1
        value = -int(ins[1]) if (ins[0] == "up") else int(ins[1])
        
        # We only want to change the aim if this is an up/down command and that's it -- no updates to position
        if index == 1:
            aim += value
            continue

        # Otherwise, we need to update both X & Y positions based on aim
        else:
            position[0] += value
            position[1] += (value * aim)

print(f"Total value: {position[0] * position[1]}")