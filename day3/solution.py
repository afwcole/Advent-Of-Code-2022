
def getItemValue(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96


def partOne(processed_rucksack_data):
    sum = 0
    for rucksack in processed_rucksack_data:
        itemsSeen = set()
        for idx, item in enumerate(rucksack):
            if idx < len(rucksack) // 2:
                itemsSeen.add(item)
            elif item in itemsSeen:
                sum += getItemValue(item)
                break
    print(sum)

def partTwo(processed_rucksack_data):
    sum = 0
    allUniqueItemsCount = {}
    for group_count, rucksack in enumerate(processed_rucksack_data):
        if group_count % 3 == 0:
            allUniqueItemsCount = {}

        uniqueRucksackItems = set()
        
        for item in rucksack:
            if item not in uniqueRucksackItems:
                if item not in allUniqueItemsCount:
                    allUniqueItemsCount[item] = 0
                allUniqueItemsCount[item] += 1

                if allUniqueItemsCount[item] == 3:
                    sum += getItemValue(item)

            uniqueRucksackItems.add(item)

    print(sum)


with open('/Users/adriancole/Desktop/Advent-Of-Code-2022/rucksack_day3/input.txt', 'r') as rucksack_file:
    rucksack_data = rucksack_file.readlines()
    processed_rucksack_data = [_.strip() for _ in rucksack_data]
    partOne(processed_rucksack_data)
    partTwo(processed_rucksack_data)
    
    
