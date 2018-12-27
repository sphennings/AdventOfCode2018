worker = 0
days = [] 

def SplitLine(line):
    date = line.split()[0].strip('[')
    time = line.split()[1].strip(']')
    event = ' '.join(line.split()[2:])
    return {'date': date, 'time': time, 'event': event}   

def TrackRest():
    line = SplitLine(lines.pop(0))
    if not line['event'].startswith('falls asleep'):
        raise Exception(f'Expected fall asleep: {line}')
    startRest = int(line['time'].split(':')[1])
    line = SplitLine(lines.pop(0))
    if not line['event'].startswith('wakes up'):
        raise Exception(f'Expected wakes up: {line}')
    endRest = int(line['time'].split(':')[1])
    return (startRest, endRest)

def StartShift():
    line = SplitLine(lines.pop(0))
    if not line['event'].startswith('Guard #'):
        raise Exception(f"Expected start of shift: {line}")
    guard = int(line['event'].split()[1].strip('#'))
    shift = ['.']*60
    while(lines and SplitLine(lines[0])['event'].startswith('falls asleep')):
        (startRest, endRest) = TrackRest()
        for i in range(startRest, endRest):
            shift[i] = '#'
    print(f'{line["date"]}: {guard}: {"".join(shift)}')
    days.append({'guard': guard, 'shift': shift})
    



if __name__ == '__main__':
    print('Part 1: ')
    lines = []
    with open('day4input.txt') as f:
        lines = f.readlines()
    lines.sort()
    while lines:
        StartShift()
    #print(days[0])
    guards = {}
    for shift in days:
        if shift['guard'] not in guards:
            guards[shift['guard']] = [0]* 60 
        for i in range(len(shift['shift'])):
            guards[shift['guard']][i] += 1 if shift['shift'][i] == '#' else 0
        #print(f'{day}: {shift["guard"]}: {"".join(shift["shift"])}')
    maxGuard = max(guards.keys(), key=lambda x: max(guards[x]))
    time = guards[maxGuard].index(max(guards[maxGuard]))
    print(f'Guard: {maxGuard}, Time: {time}, GuardTime: {maxGuard*time}')
    
    
    print('Part 2: ')
    maxGuard = max(guards.keys(), key=lambda x: sum(guards[x]))
    time = guards[maxGuard].index(max(guards[maxGuard]))
    print(f'Guard: {maxGuard}, Time: {time}, GuardTime: {maxGuard*time}')
