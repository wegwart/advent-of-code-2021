def day1(file_name):
    with open(file_name) as f:
        depth_old = None
        depth_old_old = None
        depth_sum = None
        depth_sum_old = None
        increased = 0
        for index, line in enumerate(f):
            depth = int(line.strip())
            if depth_old != None and depth_old_old != None:   
                depth_sum = depth + depth_old + depth_old_old
                print("{} ".format(depth_sum), end="")
                if depth_sum_old == None:
                    print("(not available)")            
                elif depth_sum > depth_sum_old:
                    increased += 1
                    print("(increased)")
                elif depth_sum < depth_sum_old:
                    print("(decreased)")
                else:
                    print("(equal)")            
            depth_old_old = depth_old
            depth_old = depth
            depth_sum_old = depth_sum
        print("increased => {}".format(increased))
        return increased
    
if __name__ == '__main__':
    assert(day1('day1_test.txt') == 5)
    day1('day1_puzzle.txt')
    