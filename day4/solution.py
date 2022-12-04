def is_full_overlap(elf1Lower, elf1Upper, elf2Lower, elf2Upper):
    return (elf1Lower <= elf2Lower and elf1Upper >= elf2Upper) or (elf2Lower <= elf1Lower and elf2Upper >= elf1Upper)

def is_partial_overlap(elf1Lower, elf1Upper, elf2Lower, elf2Upper):
    if (elf1Lower <= elf2Lower and elf1Upper >= elf2Lower) or (elf1Lower <= elf2Upper and elf1Upper >= elf2Upper):
        return 1
    elif (elf2Lower <= elf1Lower and elf2Upper >= elf1Lower) or (elf2Lower <= elf1Upper and elf2Upper >= elf1Upper):
        return 1
    else: 
        return 0

    # if (elf1Lower in range(elf2Lower, elf2Upper + 1)) or (elf1Upper in range(elf2Lower, elf2Upper + 1)):
    #     sum += 1
    # elif (elf2Lower in range(elf1Lower, elf1Upper + 1)) or (elf2Upper in range(elf1Lower, elf1Upper + 1)):
    #     sum += 1


with open('/Users/adriancole/Desktop/Advent-Of-Code-2022/day4/input.txt', 'r') as file:
    file_data = file.readlines()
    processed_data = [_.strip().split(",") for _ in file_data]
    
    partial_overlap_count = 0
    full_overlap_count = 0
    for row in processed_data:
        elf1Lower, elf1Upper = row[0].split("-")
        elf2Lower, elf2Upper = row[1].split("-")

        elf1Lower, elf1Upper = int(elf1Lower), int(elf1Upper)
        elf2Lower, elf2Upper = int(elf2Lower), int(elf2Upper)


        partial_overlap_count += is_partial_overlap(elf1Lower, elf1Upper, elf2Lower, elf2Upper)
        full_overlap_count += is_full_overlap(elf1Lower, elf1Upper, elf2Lower, elf2Upper)


    print(partial_overlap_count)
    print(full_overlap_count)


