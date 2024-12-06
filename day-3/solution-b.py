import re

REGEX_MATCH = "mul+\(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?,([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\)|(do\(\))|(don't\(\))"

sum_regex = 0

with open("day-3/input.txt") as f:
    data = f.read()

    matches = re.findall(REGEX_MATCH, data)
    enabled = True
    for pair in matches:
        if "do()" in pair:
            enabled = True
            continue
        elif "don't()" in pair:
            enabled = False
            continue

        if enabled:
            sum_regex += float(pair[0]) * float(pair[2])
            print(f"{pair[0]} * {pair[2]} = {float(pair[0]) * float(pair[2])}")


print(f"Sum of all the matches: {sum_regex}")