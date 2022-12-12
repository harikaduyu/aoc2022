max_calories = 0
with open('input.txt') as f:
    lines = [x.replace('\n','') for x in f.readlines()]
    current_calories = 0
    for line in lines:
        if line != '':
            current_calories += int(line)
            continue
        elif current_calories >= max_calories:
            max_calories = current_calories
        current_calories = 0


print(max_calories)





