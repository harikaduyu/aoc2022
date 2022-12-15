import copy


def get_input():

    with open('input.txt') as f:
        line = f.readline()

        # build stacks
        stacks = [[] for _ in range(len(line) // 4)]
        while line[1] != '1':
            rows = [line[i:i+4].strip() for i in range(0, len(line), 4)]
            for i, col in enumerate(rows):
                if col:
                    crate = col.replace('[','').replace(']','')
                    stacks[i].insert(0,crate)
            line = f.readline()

        #get moves
        moves = []
        while line:
            line = f.readline()
            if line[0:4] == 'move':
                _, move_, _, from_, _, to_ = line.strip().split(" ")
                moves.append((
                    int(move_),
                    int(from_) -1,
                    int(to_) - 1,
                ))

        return stacks, moves



def move1(stacks, move_, from_, to_):
    for _ in range(move_):
        x = stacks[from_].pop()
        stacks[to_].append(x)


def move2(stacks,move_, from_, to_):

    stacks[to_] += stacks[from_][- move_:]
    del stacks[from_][- move_:]


if __name__ == '__main__':
    stacks1, moves = get_input()
    stacks2 = copy.deepcopy(stacks1)
    for (move_, from_, to_) in moves:
        move1(stacks1, move_, from_, to_)
        move2(stacks2, move_, from_, to_)
    top1 = ''
    top2 = ''
    for i in range(len(stacks1)):
        top1 += stacks1[i][-1] if stacks1[i] else ''
        top2 += stacks2[i][-1] if stacks1[i] else ''
    print(top1)
    print(top2)
