# from aoc2022 import get_input
from typing import List


def get_input() -> List[str]:

    with open('input.txt') as f:
        num_pairs = [line.strip().split(',') for line in f.readlines()]
    return num_pairs


def does_one_range_contain_the_other(two_ranges: List[str]) -> bool:
    print(two_ranges)
    ranges = []
    for num_pair in two_ranges:
        start, end = num_pair.split('-')
        ranges.append(set(range(int(start), int(end) + 1)))

    intersection = ranges[0] & ranges[1]
    return len(intersection) == len(ranges[0]) or len(intersection) == len(ranges[1])


def does_one_range_intersect_with_the_other(two_ranges: List[str]) -> bool:
    print(two_ranges)
    ranges = []
    for num_pair in two_ranges:
        start, end = num_pair.split('-')
        ranges.append(set(range(int(start), int(end) + 1)))

    intersection = ranges[0] & ranges[1]
    return len(intersection) > 0


if __name__ == '__main__':
    range_pairs_list = get_input()
    count_contains_the_other = 0
    count_intersects = 0
    for two_ranges in range_pairs_list:
        if does_one_range_contain_the_other(two_ranges=two_ranges):
            count_contains_the_other += 1
        if does_one_range_intersect_with_the_other(two_ranges=two_ranges):
            count_intersects += 1
    print(count_contains_the_other)
    print(count_intersects)
