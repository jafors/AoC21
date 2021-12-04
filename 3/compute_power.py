from collections import Counter

def to_decimal(binary):
    decimal = 0
    for i in range(0, len(binary)):
        decimal += (2 ** i) * int(binary[len(binary) - 1 - i])
    return decimal

def most_common_bits(binaries):
    counts = ([Counter(col).most_common() for col in zip(*binaries)])
    binary = []
    for e in counts:
        if len(e) == 1:
            binary.append(e[0][0])
        elif e[0][1] == e[1][1]:
            binary.append("1")
        else:
            binary.append(e[0][0])
    return binary

def least_common_bits(binaries):
    counts = ([Counter(col).most_common() for col in zip(*binaries)])
    binary = []
    for e in counts:
        if len(e) == 1:
            binary.append(e[0][0])
        elif e[0][1] == e[1][1]:
            binary.append("0")
        else:
            binary.append(e[1][0])
    return binary

def select_binaries(binaries, which):
    for i in range(0, len(binaries[0])):
        new_binaries = []
        if which == "most":
            bit =  most_common_bits(binaries)[i]
        else:
            bit =  least_common_bits(binaries)[i]
        for r in binaries:
            if r[i] == bit:
                new_binaries.append(r)
        binaries = new_binaries
        if len(binaries) == 1:
            return(binaries[0])
 

binaries = []

binary_input = open("binary_input.txt", 'r')
for line in binary_input:
    binary = list(line.rstrip())
    binaries.append(binary)

most_common = most_common_bits(binaries)
least_common = ["0" if m == "1" else "1" for m in most_common]

gamma = to_decimal(most_common)
epsilon = to_decimal(least_common)
print("Power consumption = " + str(gamma * epsilon))

oxygen = select_binaries(binaries, "most") #, most_common[0])
co2 = select_binaries(binaries, "least") # , least_common[0])
#print(most_common)
print(to_decimal(oxygen) * to_decimal(co2))

