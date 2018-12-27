def reduce(polymer):
    changed = True
    #print(''.join(polymer))
    while changed:
        changed = False
        i = 0
        while i < len(polymer) - 1:
            if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
                del polymer[i:i+2]
                changed = True
            else:
                i += 1
    return polymer

if __name__ == '__main__':
    lines = []
    with open('day5input.txt') as f:
        lines = f.readlines()
    print('Part 1: ')
    #polymer = reduce(list("dabAcCaCBAcCcaDA"))
    polymer = reduce(list(lines[0].strip()))

    print(len(polymer))
    print('Part 2: ')
    print(min([len(reduce([l for l in polymer if l.lower() != letter])) for letter in list("abcdefghijklmnopqrstuvwxyz")]))
    