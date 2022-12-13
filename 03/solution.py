from typing import List, Callable
from collections import Counter

def get_input() -> List[str] :

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def find_common_item_type(rucksack_items: str) -> str:
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

def get_common_item_between_3_elves(chunk: List[List[str]]) -> str:

    combined_set_of_unique_values_from_3_elves = ''
    for items in chunk:
        unique_items_of_rucksack_combined = ''.join(list(set(list(items))))
        combined_set_of_unique_values_from_3_elves += unique_items_of_rucksack_combined
    counter = Counter(combined_set_of_unique_values_from_3_elves)
    counter_ordered_by_most_common = counter.most_common()
    assert counter_ordered_by_most_common[0][1] == 3
    return counter_ordered_by_most_common[0][0]


def sum_priorities(input_list: List[str] | List[List[str]], func: Callable) -> None:
    total_priorities = 0
    for line in input_list:
        char = func(line)
        priority = get_priority_of_char(char)
        total_priorities += priority

    print("total priorities ", total_priorities)
    # return total_priorities

def sum_priorities_part_2():
    ...


if __name__ == '__main__':
    lines = get_input()
    print("Part 1")
    sum_priorities(lines, find_common_item_type)

    print("Part 2")
    chunks_of_3 = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    sum_priorities(chunks_of_3, get_common_item_between_3_elves)
    # sum_priorities_part_2(lines)

