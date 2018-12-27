if __name__ == '__main__':
    with open('day3input.txt') as f:
        lines = f.readlines()
        #lines = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        print('Part 1: ')
        fabric = [None] * 1000
        for i in range(len(fabric)):
            fabric[i] = ['.'] * 1000

        

        for line in lines:
            parts = line.split()
            id = parts[0].strip('#')
            posPart = parts[2]
            dimPart = parts[3]
            xpos = int(posPart.split(',')[0])
            ypos = int(posPart.split(',')[1].strip(':'))
            width = int(dimPart.split('x')[0])
            height = int(dimPart.split('x')[1])
            for x in range(width):
                for y in range(height):
                    if fabric[y+ypos][x+xpos] == '.':
                        fabric[y+ypos][x+xpos] = id
                    else:
                        fabric[y+ypos][x+xpos] = 'X'

        
        overlapp = sum((row.count('X') for row in fabric))
        
        print(overlapp)
        print('Part 2: ')
        for line in lines:
            parts = line.split()
            id = parts[0].strip('#')
            posPart = parts[2]
            dimPart = parts[3]
            xpos = int(posPart.split(',')[0])
            ypos = int(posPart.split(',')[1].strip(':'))
            width = int(dimPart.split('x')[0])
            height = int(dimPart.split('x')[1])
            overlapped = False
            for x in range(width):
                for y in range(height):
                    if fabric[y+ypos][x+xpos] != id:
                        overlapped = True
            if not overlapped:
                print(id)