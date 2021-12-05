def day4(file_name, size):
    with open(file_name) as f:
        width = size
        height = size
        bingo_boards = list()
        bingo_board_masks = list()
        for line_index, line in enumerate(f):
            # read random numbers
            if line_index == 0:
                random_numbers = list(map(lambda x: int(x), line.strip().split(',')))
                continue
            # read bingo boards
            if len(line.strip()) < width:
                count_rows = 0
                bingo_board = [[0 for x in range(width)] for y in range(height)] 
                bingo_board_mask = [[False for x in range(width)] for y in range(height)] 
                continue
            bingo_board[count_rows] = list(map(lambda x: int(x), line.strip().split()))
            count_rows += 1
            if count_rows == height:
                bingo_boards.append(bingo_board)
                bingo_board_masks.append(bingo_board_mask)
            continue
        # find number in board
        found = False
        for random_number in random_numbers:
            for board_index, board in enumerate(bingo_boards):
                for row_index, row in enumerate(board):
                    for col_index, col in enumerate(row):
                        if col == random_number:
                            bingo_board_masks[board_index][row_index][col_index] = True
            # find full columns and rows 
            for board_index, board_mask in enumerate(bingo_board_masks):
                for x in range(width):
                    count = 0
                    for y in range(height):
                        if board_mask[y][x] == True:
                            count += 1
                    if count == height:
                        print('Found full col {} in board {}'.format(x, board_index))
                        found = True
                for y in range(height):
                    count = 0
                    for x in range(width):
                        if board_mask[y][x] == True:
                            count += 1
                    if count == width:
                        print('Found full row {} in board {}'.format(y, board_index))
                        found = True
                if found == True:
                    print('Just called number {}'.format(random_number))
                    # calculate sum of all unmarked numbers in board
                    unmarked_sum = 0
                    board = bingo_boards[board_index]
                    board_mask = bingo_board_masks[board_index]
                    for row_index, row in enumerate(board_mask):
                        for col_index, col in enumerate(row):
                            if board_mask[row_index][col_index] == False:
                                number = board[row_index][col_index] 
                                unmarked_sum += number
                    # calcuate final score
                    print('{} * {} => {}'.format(random_number, unmarked_sum, random_number * unmarked_sum))
                    return random_number * unmarked_sum

if __name__ == '__main__':
    assert(day4('day4_test.txt', 5) == 4512)
    day4('day4_puzzle.txt', 5)
