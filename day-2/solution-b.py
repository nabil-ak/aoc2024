good_reports = 0

with open("day-2/input.txt") as f:
    lines = f.readlines()
    
    for line in lines:
        bad = 0
        line_splitted = line.split()
        increase_or_decrease = None

        for x in range(len(line_splitted)-1):
            first_num = int(line_splitted[x])
            second_num = int(line_splitted[x+1])
            dif = abs(first_num - second_num)
            if 1 > dif or dif > 3:
                print(f"Bad report: {line} and first_num: {first_num} and second_num: {second_num}")
                bad+=1
                if bad > 1:
                    break   
            
            if increase_or_decrease is None:
                if first_num < second_num:
                    increase_or_decrease = "increase"
                elif first_num > second_num:
                    increase_or_decrease = "decrease"
            else:
                if increase_or_decrease == "increase" and first_num > second_num or increase_or_decrease == "decrease" and first_num < second_num:
                    bad+=1
                    if bad > 1:
                        break   

        if bad <= 1:        
            good_reports += 1

print(good_reports)
        