if __name__ == '__main__':
    with open('day1input.txt') as f:
        print('Part 1: ')
        lines = f.readlines()
        numbers = list(map(int, lines))
        print(sum(numbers))

        print('part 2:')
        frequencies = set([0])
        freq = 0
        index = 0
        while True: 
            change = numbers[index%len(numbers)]
            index +=1
            freq += change
            if freq in frequencies:
                print(freq)
                break
            frequencies.add(freq)
