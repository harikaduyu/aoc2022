
def get_input():
    with open('input.txt') as f:
        line = f.readline()
    return line

def get_first_non_repeated_window_of_length(line, num_chars):
    d = {}
    length = 0
    start = 0
    for i, char in enumerate(line):
        if char in d and start <= d[char]:
            start = d[char] + 1
        else:
            length = i + 1 - start
        d[char] = i

        if length == num_chars:
            print(i + 1)
            break

if __name__ == '__main__':
    line = get_input()
    print("Part 1")
    get_first_non_repeated_window_of_length(line, 4)
    print("Part 2")
    get_first_non_repeated_window_of_length(line, 14)


