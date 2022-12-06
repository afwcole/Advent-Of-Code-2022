def solution1(interval, line):
    for start in range(0, len(line)):
        if (len(set(line[start : start + interval])) == interval):
            return start + interval

with open('/Users/adriancole/Desktop/Advent-Of-Code-2022/day6/input.txt', 'r') as file:
    file_data = file.readlines()
    print(solution1(4, file_data[0]))
    print(solution1(14, file_data[0]))

    
        
