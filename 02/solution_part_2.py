#trying another approach for part 2 https://github.com/jacopofar/advent2022/blob/main/advent2022/day02.py
from typing import List
solution_map = {
    'AX': 3,
    'BX': 1,
    'CX': 2,
    'AY': 4,
    'BY': 5,
    'CY': 6,
    'AZ': 8,
    'BZ': 9,
    'CZ': 7,
}

def get_input() -> List[str] :

    with open('input.txt') as f:
        lines = [line.strip().replace(' ','') for line in f.readlines()]
    return lines

def calculate_score(input_lines: List[str])-> int:
    total_score = 0
    for line in input_lines:
        total_score += solution_map[line]
    return total_score

if __name__ == '__main__':
    lines = get_input()
    score = calculate_score(lines)
    print(f"Total score is: {score}")