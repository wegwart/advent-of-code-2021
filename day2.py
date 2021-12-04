
def day2(file_name):
    with open(file_name) as f:
        horizontal = 0
        depth = 0
        for index, line in enumerate(f):
            splitted_line = line.split(' ')
            direction = splitted_line[0]
            distance = int(splitted_line[1])
            if direction == 'forward':
                horizontal += distance
                print('forward {} adds {} to your horizontal position, a total of {}.'.format(distance, distance, horizontal))
            elif direction == "down":
                depth += distance
                print('down {} adds {} to your depth, resulting in a value of {}.'.format(distance, distance, depth))
            elif direction == "up":
                depth -= distance
                print('up {} adds {} to your depth, resulting in a value of {}.'.format(distance, distance, depth))
        print("{} * {} => {}".format(horizontal, depth, horizontal * depth))
        return horizontal * depth

if __name__ == '__main__':
    assert(day2('day2_test.txt') == 150)
    day2('day2_puzzle.txt')
