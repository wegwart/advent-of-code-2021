def day1(file_name):
    with open(file_name) as f:
        depth_old = None
        increased = 0
        for index, line in enumerate(f):
            depth = int(line.strip())
            print("{} ".format(depth), end="")
            depth = int(line.strip())
            if depth_old == None:
                print("(not available)")            
            elif depth > depth_old:
                increased += 1
                print("(increased)")
            elif depth < depth_old:
                print("(decreased)")
            else:
                print("(equal)")            
            depth_old = depth
        print("increased => {}".format(increased))
        return increased

if __name__ == '__main__':
    assert(day1('day1_test.txt') == 7)
    day1('day1_puzzle.txt')

    