def depth_increase(depths, i):
    if i == 0:
        return "NA - no previous depth"
    else:
        if depths[i] > depths[i - 1]:
            return "increased"
        elif depths[i] < depths[i - 1]:
            return "decreased"
        else:
            return "no change in depth"

def create_trio_sums(depths):
    sums = []
    for i in range(0, len(depths) - 2):
        trio_sum = sum(depths[i:i+3])
        sums.append(trio_sum)
    return sums

depth_file = open("sonar_depths.txt", "r")
depths = []
depth_change = []
for line in depth_file:
    if line == "\n" or line == "":
        continue
    depths.append(int(line.rstrip()))
for i in range(0, len(depths)):
    depth_change.append(depth_increase(depths, i))
print("Single sonar depth increas8ed {} times".format(depth_change.count("increased")))

sums = create_trio_sums(depths)
print(len(sums))
print(len(depths))
depth_sum_change = []
for i in range(0, len(sums)):
    depth_sum_change.append(depth_increase(sums, i))
print("Sum sonar depth increased {} times".format(depth_sum_change.count("increased")))

