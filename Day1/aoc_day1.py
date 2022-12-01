
def mostCalories(calories_data):
    max_calories, current_elf_calories = 0, 0
    all_elves_calories = []

    for line in calories_data:
        calorie = line[:-1]
        if len(calorie) == 0:
            max_calories = max(max_calories, current_elf_calories)
            all_elves_calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(calorie)

    sum_of_top3_calorie_elves = sum(sorted(all_elves_calories, reverse=True)[:3])
    return max_calories, sum_of_top3_calorie_elves

with open('calories.txt', 'r') as calories_file:
    calories_data = calories_file.readlines()
    print(mostCalories(calories_data))
    
