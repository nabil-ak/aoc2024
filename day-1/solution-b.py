left = []
right = []
right_counter = {}

similarity_score = 0

with open("day-1/input.txt") as f:
    lines = f.readlines()
    
    for line in lines:
        line_splitted = line.split("   ")

        left_number = int(line_splitted[0])
        right_number = int(line_splitted[1].replace("\n", ""))

        left.append(left_number)
        right.append(right_number)

        right_counter[right_number] = right_counter.get(right_number, 0) + 1


for number in left:
    similarity_score += right_counter.get(number, 0)*number

print(similarity_score)