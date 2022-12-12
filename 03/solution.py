from typing import List


def get_input() -> List[str] :

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def find_common_item_type(rucksack_items: str) -> str:
    print("rucksack_items: ",rucksack_items)
    half_size = len(rucksack_items) // 2

    first_half_unique_values = set(rucksack_items[0:half_size])


    second_half_unique_values = set(rucksack_items[half_size:len(rucksack_items)])

    two_halves_combined_list = list(first_half_unique_values) + list(second_half_unique_values)

    count_dict = {}
    for char in two_halves_combined_list:
        count_dict[char] = count_dict.get(char,0) + 1 
        if count_dict[char] == 2:
            return char


def get_priority_of_char(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


if __name__ == '__main__':
    lines = get_input()
    total_priorities = 0
    for line in lines:
        char = find_common_item_type(line)
        priority = get_priority_of_char(char)
        total_priorities += priority
    print(total_priorities)
