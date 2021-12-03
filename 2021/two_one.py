# declare stuff ahead of time -- force of habit
position = [0, 0]

with open('./input/2.txt', 'r') as instructions:
    for line in instructions:
        # Parsing nonsense
        ins = line.split(" ")
        index = 0 if ins[0] == "forward" else 1
        value = -int(ins[1]) if (ins[0] == "up") else int(ins[1])
        
        # Update the relevant position
        position[index] += value

print(f"Total value: {position[0] * position[1]}")