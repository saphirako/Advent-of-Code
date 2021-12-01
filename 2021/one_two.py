numOfIncreases = 0
prevValue = 10000000000000

# NOTE:     I don't like how this processes input. Since it's only 2k lines, it's nothing but if we
#               wanted a general solution, not loading the whole thing into memory all at once
#               would be preferable. 🙃
with open('./input/1.txt', 'r') as layers:
    values = list(map(int, layers.readlines()))

for i in range(0, len(values)-2):
    numOfIncreases += 1 if (values[i] + values[i+1] + values[i+2]) > prevValue else 0
    prevValue = values[i] + values[i+1] + values[i+2]

print(f"Number of increases: {numOfIncreases}")