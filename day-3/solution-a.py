import re

REGEX_MATCH = "mul+\(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?,([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\)"

sum_regex = 0

with open("day-3/input.txt") as f:
    data = f.read()

    matches = re.findall(REGEX_MATCH, data)
    for pair in matches:
        sum_regex += float(pair[0]) * float(pair[2])
        print(f"{pair[0]} * {pair[2]} = {float(pair[0]) * float(pair[2])}")


print(f"Sum of all the matches: {sum_regex}")