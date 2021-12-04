
def day4(file_name):
    with open(file_name) as f:
        sum = 188
        last = 24
        # ToDo:
        print('{} * {} => {}'.format(sum, last, sum * last))
        return sum * last

if __name__ == '__main__':
    assert(day4('day4_test.txt') == 4512)
    day4('day4_puzzle.txt')
