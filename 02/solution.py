from typing import List
shapes_score = {
    'rock': 1,
    'paper': 2,
    'scissors':3
}

game_scores = {
    'draw': 3,
    'win': 6,
    'lose': 0
}

elf_shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

player_shapes = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


def get_input(file_name: str) -> List[List[str]]:
    with open(file_name) as f:
        lines = [line.strip().split(' ') for line in  f.readlines()]
        return lines

def calculate_points_for_round(line: List[str]) -> int:
    score = 0
    elf_shape = elf_shapes[line[0]]
    player_shape = player_shapes[line[1]]
    if player_shape == elf_shape:
        score += game_scores['draw']
    elif player_shape == 'rock':
        if elf_shape == 'paper':
            score += game_scores['lose']
        else:
            score += game_scores['win']
    elif player_shape == 'paper':
        if elf_shape == 'scissors':
            score += game_scores['lose']
        else:
            score += game_scores['win']
    elif player_shape == 'scissors':
        if elf_shape == 'rock':
            score += game_scores['lose']
        else:
            score += game_scores['win']
    score += shapes_score[player_shape]
    return score

def calculate_score_given_strategy(line: str) -> int:
    score = 0
    elf_shape = elf_shapes[line[0]]
    player_shape = player_shapes[line[1]]
    if player_shape == elf_shape:
        score += game_scores['draw']
    elif player_shape == 'rock':
        if elf_shape == 'paper':
            score += game_scores['lose']
        else:
            score += game_scores['win']
    elif player_shape == 'paper':
        if elf_shape == 'scissors':
            score += game_scores['lose']
        else:
            score += game_scores['win']
    elif player_shape == 'scissors':
        if elf_shape == 'rock':
            score += game_scores['lose']
        else:
            score += game_scores['win']
    score += shapes_score[player_shape]
    return score



if __name__ == '__main__':
    lines = get_input('input.txt')
    total_score = 0
    for line in lines:
        total_score += calculate_points_for_round(line)
    print(f"Total score: {total_score}")