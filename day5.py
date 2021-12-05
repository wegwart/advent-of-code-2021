def day5(file_name, size):
    with open(file_name) as f:
        width = size
        height = size
        ones = 0
        twos = 0
        # ToDo:
        lut = [[0 for x in range(width)] for y in range(height)] 

        for index, line in enumerate(f):
            line = line.strip()
            x1 = int((line.split(' ')[0]).split(',')[0])
            y1 = int((line.split(' ')[0]).split(',')[1])
            x2 = int((line.split(' ')[2]).split(',')[0])
            y2 = int((line.split(' ')[2]).split(',')[1])
            if x1 == x2:
                print("vertiacal line {}".format(line)) 
                if y2 < y1:
                    for y in range(y2,y1+1):
                        lut[y][x1] += 1
                else:
                    for y in range(y1,y2+1):
                        lut[y][x1] += 1
            elif y1 == y2:
                print("horizontal line {}".format(line))   
                if x2 < x1:
                    for x in range(x2,x1+1):
                        lut[y1][x] += 1  
                else:
                    for x in range(x1,x2+1):
                        lut[y1][x] += 1  
            else:
                print("skip line {}".format(line))         
        for y in range(height):
            for x in range(width):
                if lut[y][x] == 1:
                    ones += 1
                if lut[y][x] > 1:
                    twos += 1

        print('{} {}'.format(ones, twos))
        return twos

if __name__ == '__main__':
    assert(day5('day5_test.txt', 10) == 5)
    day5('day5_puzzle.txt', 1000)
