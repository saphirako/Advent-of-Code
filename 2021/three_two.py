# declare stuff ahead of time -- force of habit
top = {
    "count": 0,
    "length": 0
    # "0": {}
    # "1": {}
}

with open('./input/3.txt', 'r') as lines:
    # For each line, create dictionary keys or increment them if we've already seen it
    for line in lines:
        # Reset to top level
        level = top
        level["count"] += 1
        top["length"] = len(line)-1


        for bit in line:
            if bit == "/n":
                break
                
            # Create a new node if we haven't seen it before ({this will only happen in the first bit...)
            if bit not in level.keys():
                level[bit] = {
                    "count": 0
                }
            
            level[bit]["count"] += 1
            level = level[bit]

# calculate CO2 & O2 decimals realtime
o2 = ["", top]
co2 = ["", top]
o2_done = False
co2_done = False

for index in range(0, top["length"]):
    # check for keys -- if one doesn't exist, check the count of the other value
    # if 1 -- we're done
    # if more -- keep going

    o2_pivot = "1" if o2[1]["1"]["count"] >= o2[1]["0"]["count"] else "0"
    o2[0] = f"{o2[0]}{o2_pivot}"
    o2[1] = o2[1][o2_pivot]

    co2_pivot = "1" if co2[1]["1"]["count"] < co2[1]["0"]["count"] else "0"
    co2[0] = f"{co2[0]}{co2_pivot}"
    co2[1] = co2[1][co2_pivot] 

    # CURRENT PROBLEM: If a key does not exist, we crash -- see the notes on line 39-41 for
    #                   how to fix. 

print(f"O2: {int(o2[0], 2)}\t\tCO2: {int(co2[0], 2)}")
print(f"Total value: {int(o2[0], 2) * int(co2[0], 2)}")