numOfIncreases = 0
prevValue = 10000000000000

with open('./input/1.txt', 'r') as layers:
    for line in layers:
        numOfIncreases += 1 if int(line) > prevValue else 0
        prevValue = int(line)

print(f"Number of increases: {numOfIncreases}")