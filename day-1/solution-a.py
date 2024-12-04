left = []
right = []

diff = 0

with open("day-1/input.txt") as f:
    lines = f.readlines()
    
    for line in lines:
        line_splitted = line.split("   ")
        left.append(int(line_splitted[0]))
        right.append(int(line_splitted[1].replace("\n", "")))

left.sort()
right.sort()


for pair in zip(left, right):
    if pair[1] > pair[0]:
        diff += pair[1] - pair[0]
    else:
        diff += pair[0] - pair[1]
    
print(diff)