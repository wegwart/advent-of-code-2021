with open('day1.txt') as f:
    depth_old = None
    depth_old_old = None
    depth_sum = None
    increased = 0
    for index, line in enumerate(f):
        depth = int(line.strip())
        print("{} ".format(depth), end="")
        depth = int(line.strip())
        if depth_old != None and depth_old_old != None:   
            depth_sum = depth + depth_old + depth_old_old
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
        depth_old_old = depth_old
        depth_sum_old = depth_sum
    print("increased => {}".format(increased))

    