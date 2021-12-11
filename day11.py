import sys
import time

class Esc:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   ZERO_BOLD = BOLD + '0' + END
   def MoveUp(n): return '\x1b[{}A'.format(n)
   def MoveDown(n): return '\x1b[{}B'.format(n)
   def MoveRight(n): return '\x1b[{}C'.format(n)
   def MoveLeft(n): return '\x1b[{}D'.format(n)

def readGrid(file_name, size):
    with open(file_name) as f:
        grid = [[0 for row in range(size)] for col in range(size)]
        for row, line in enumerate(f):
            for col in range(size):
                grid[row][col] = int(line[col])
    return grid

def incrementGrid(grid, size):
    for row in range(size):
        for col in range(size):
            grid[row][col] += 1

def flashGrid(grid, size):
    flashes = 0
    for row in range(size):
        for col in range(size):
            if grid[row][col] > 9:
                for rrow in range(row-1,row+2):
                    if rrow >= 0 and rrow < size:
                        for ccol in range(col-1,col+2):
                            if ccol >= 0 and ccol < size:
                                if grid[rrow][ccol] != 0:                     
                                    grid[rrow][ccol] += 1
                grid[row][col] = 0
                flashes += 1
    return flashes

def printGrid(grid, size):
    for row in range(size):
        line = ""
        for col in range(size):
            if grid[row][col] == 0:
                line += Esc.ZERO_BOLD
            else: 
                line += chr(ord('0') + grid[row][col])
        print(line) 

def day11(file_name, size, steps):
    flashes = 0
    grid = readGrid(file_name, size)
    print('Befor any steps:')
    printGrid(grid, size) 
    for step in range(steps):
        if step > 0 and step < steps: 
            sys.stdout.write(Esc.MoveUp(size+2))
            sys.stdout.flush()
        incrementGrid(grid, size)
        while True:
            fflashes = flashGrid(grid, size)
            if fflashes == 0:
                break
            flashes += fflashes
        print('After step {}:'.format(step+1))
        printGrid(grid, size) 
        print('Flashes {}'.format(flashes))
        time.sleep(0.1)
    return flashes

if __name__ == '__main__':
    assert(day11('day11_test5x5.txt', 5, 2) == 9)
    assert(day11('day11_test.txt', 10, 10) == 204)
    assert(day11('day11_test.txt', 10, 100) == 1656)
    day11('day11_puzzle.txt', 10, 100)
