def day5(file_name):
    with open(file_name) as f:
        a = 2
        b = 3
        # ToDo:
        print('{} * {} => {}'.format(a, b, a * b))
        return a * b

if __name__ == '__main__':
    assert(day5('day5_test.txt') == 6)
    day5('day5_puzzle.txt')
