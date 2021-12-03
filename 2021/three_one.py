# declare stuff ahead of time -- force of habit
bits = []
line_count = 0

def calculate_bits(line):
    # Increment each index by 1 or 0 
    for index in range(0, len(line)-1):
        bits[index] += int(line[index])
    
    # used to increment line_count
    return 1


with open('./input/3.txt', 'r') as lines:
    line = lines.readline()

    # used to make this solution work for any size input
    bits = [0] * (len(line)-1)
    line_count += calculate_bits(line)

    # loop the rest
    for line in lines:
        line_count += calculate_bits(line)

# calculate gamma & epsilon decimals realtime
γ = 0
ε = 0

for index in reversed(range(0, len(bits))):
    # If the value of the bits array is greater than half of the total lines, it's used in over
    # half of the input, meaning it's more common
    γ += pow(2, (len(bits)-index-1)) if bits[index] > (line_count / 2) else 0
    
    # Epsilon is the inverse of gamma so reverse the size comparison of line_count
    ε += pow(2, (len(bits)-index-1)) if bits[index] < (line_count / 2) else 0

print(f"Bits: {bits}")
print(f"Gamma: {γ}\nEpsilon: {ε}")
print(f"Total value: {γ * ε}")