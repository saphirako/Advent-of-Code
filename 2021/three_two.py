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
        top["length"] = len(line)


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
o2_keys = [True, True]
co2_keys = [True, True]

for index in range(0, top["length"]):
    # #############################
    #       Calculate Oxygen
    # #############################
    # Ensure 0 and 1 keys exist
    o2_keys[0] = "0" in o2[1].keys()
    o2_keys[1] = "1" in o2[1].keys()

    # If we have both keys present, proceed as normal
    if all(o2_keys):
        o2_pivot = "1" if o2[1]["1"]["count"] >= o2[1]["0"]["count"] else "0"

    # If not, select the only one present
    elif any(o2_keys):
        o2_pivot = "0" if o2_keys[0] else "1"

    # Add the bit to the string and go to the next node
    o2[0] = f"{o2[0]}{o2_pivot}"
    o2[1] = o2[1][o2_pivot]


    # #############################
    #   Calculate Carbon Dioxide
    # #############################
    # Ensure 0 and 1 keys exist
    co2_keys[0] = "0" in co2[1].keys()
    co2_keys[1] = "1" in co2[1].keys()

    # If we have both keys present, proceed as normal
    if all(co2_keys):
        co2_pivot = "1" if co2[1]["1"]["count"] < co2[1]["0"]["count"] else "0"

    # If not, select the only one present
    elif any(co2_keys):
        co2_pivot = "0" if co2_keys[0] else "1"

    # Add the bit to the string and go to the next node
    co2[0] = f"{co2[0]}{co2_pivot}"
    co2[1] = co2[1][co2_pivot]

print(f"O2: {int(o2[0], 2)}\t\tCO2: {int(co2[0], 2)}")
print(f"Total value: {int(o2[0], 2) * int(co2[0], 2)}") 