
def day3(file_name, width):
    with open(file_name) as f:
        gamma = 0
        epsilon = 0
        lut_ones = [0] * width
        lut_zeros = [0] * width
        for index, line in enumerate(f):
            value = int(line.strip(), 2)
            for i in range(width):
                mask = 1 << i
                if (value & mask) == mask:
                    lut_ones[i] += 1
                else:
                    lut_zeros[i] += 1
        for i in range(width):
            mask = 1 << i
            if lut_ones[i] > lut_zeros[i]:
                gamma += mask
            else:
                epsilon += mask
        print('{} * {} => {}'.format(gamma, epsilon, gamma * epsilon))
        return gamma * epsilon

if __name__ == '__main__':
    assert(day3('day3_test.txt', 5) == 198)
    day3('day3_puzzle.txt', 12)
