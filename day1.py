with open('day1.txt') as f:
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
        elif depth > depth_old:
            print("(increased)")
        else:
            print("(equal)")            
        depth_old = depth
    print("increased => {}".format(increased))

    