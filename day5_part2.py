def day5(file_name, size):
    with open(file_name) as f:
        width = size
        height = size
        count = 0
        lut = [[0 for x in range(width)] for y in range(height)] 

        for index, line in enumerate(f):
            line = line.strip()
            x1 = int((line.split(' ')[0]).split(',')[0])
            y1 = int((line.split(' ')[0]).split(',')[1])
            x2 = int((line.split(' ')[2]).split(',')[0])
            y2 = int((line.split(' ')[2]).split(',')[1])
            if x1 == x2:
                print("vertical line {}".format(line)) 
                if y2 < y1:
                    yit = iter(range(y2,y1+1))
                else:
                    yit = iter(range(y1,y2+1))   
                for y in yit:
                    lut[y][x1] += 1       
            elif y1 == y2:
                print("horizontal line {}".format(line))  
                if x2 < x1:
                    xit = iter(range(x2,x1+1))
                else:
                    xit = iter(range(x1,x2+1)) 
                for x in xit:
                    lut[y1][x] += 1        
            else:
                print("diagonal line {}".format(line))
                if x2 < x1:
                    xit = iter(range(x1,x2-1,-1))
                else:
                    xit = iter(range(x1,x2+1)) 
                if y2 < y1:
                    yit = iter(range(y1,y2-1,-1))
                else:
                    yit = iter(range(y1,y2+1)) 
                for x in xit:
                    y = next(yit)
                    lut[y][x] += 1                        
 
        for y in range(height):
            for x in range(width):
                if lut[y][x] >= 2:
                    count += 1

        print('{}'.format(count))
        return count

if __name__ == '__main__':
    assert(day5('day5_test.txt', 10) == 12)
    day5('day5_puzzle.txt', 1000)
