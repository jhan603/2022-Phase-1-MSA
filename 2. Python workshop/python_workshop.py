from pprint import pprint

transmissions = []
with open("transmissions.csv") as file:
    for line in file:
        line = line.strip()
        transmissions.append(line.split(","))
pprint(transmissions)

transmissions.pop(0)
ids = [row[0] for row in transmissions]
transmissions = [row[1] for row in transmissions]
sums = []
for t in transmissions:
    current_sum = 0
    for char in t:
        try:
            current_sum += int(char)
        except:
            continue
    sums.append(current_sum)
print(sums)

freq_dict = {int(ids[i]):sums[i] for i in range(len(ids))}
freq_tuples = sorted(freq_dict.items())
message = ""
for item in freq_tuples:
    message += chr(item[1])
print(message)