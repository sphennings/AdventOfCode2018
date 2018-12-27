import itertools

if __name__ == '__main__':
    with open('day2input.txt') as f:
        print('Part 1: ')
        lines = f.readlines()
        has2 = 0
        has3 = 0
        for line in lines:
            counts = [line.count(c) for c in set(line)]
            if 2 in counts:
                has2 += 1
            if 3 in counts:
                has3 += 1
        print(f"Checksum: {has2 * has3}")
        print('Part 2: ')
        for (w1, w2) in itertools.combinations(lines, 2):
            difference = sum((1 for i in range(len(w1)) if w1[i] != w2[i]))
            if difference == 1: 
                print("".join(w1[i] for i in range(len(w1)) if w1[i] == w2[i]))
                

