
def day2(file_name):
    with open(file_name) as f:
        horizontal = 0
        depth = 0
        aim = 0
        for index, line in enumerate(f):
            splitted_line = line.split(' ')
            direction = splitted_line[0]
            distance = int(splitted_line[1])
            if direction == 'forward':
                horizontal += distance
                depth += aim * distance 
                print('forward {} adds {} to your horizontal position, a total of {}. Because'.format(distance, distance, horizontal))
                if aim == 0:
                    print('your aim is 0, your depth does not change.')
                else:
                    print('your aim is {}, your depth increases by {}*{}={} to a total of {}.'.format(aim, aim, distance, aim * distance, depth))
            elif direction == "down":
                aim += distance
                print('down {} adds {} to your aim, resulting in a value of {}.'.format(distance, distance, aim))
            elif direction == "up":
                aim -= distance
                print('up {} adds {} to your aim, resulting in a value of {}.'.format(distance, distance, aim))
        print("{} * {} => {}".format(horizontal, depth, horizontal * depth))
        return horizontal * depth

if __name__ == '__main__':
    assert(day2('day2_test.txt') == 900)
    day2('day2_puzzle.txt')
