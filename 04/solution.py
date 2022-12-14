# from aoc2022 import get_input
from typing import List
import re


def get_input() -> List[str]:
    range_pairs = []
    with open('input.txt') as f:
        for line in f.readlines():
            start1, end1, start2, end2, _ = re.split(r"[^0-9]",line)
            range_1 = range(int(start1), int(end1) + 1) 
            range_2 = range(int(start2), int(end2) + 1) 
            range_pairs.append([range_1, range_2])
    return range_pairs


def get_part1(range_pairs: List[range]) -> bool:
    count = 0
    for r in range_pairs:
        intersection = set(r[0]) & set(r[1])
        if len(intersection) == len(r[0]) or len(intersection) == len(r[1]):
            count +=1
    return count



def get_part2(range_pairs: List[range]) -> bool:
    # print(two_ranges)
    count = 0
    for r in range_pairs:
        intersection = set(r[0]) & set(r[1])
        if len(intersection) > 0:
            count += 1
    return count


if __name__ == '__main__':
    range_pairs = get_input()
    count_one_contains_other = get_part1(range_pairs=range_pairs)
    print(count_one_contains_other)
    count_intersects = get_part2(range_pairs=range_pairs)
    print(count_intersects)
