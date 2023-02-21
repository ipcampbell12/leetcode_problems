sud = [[7, 8, 4, 1, 5, 9, 3, 2, 6],
       [5, 3, 9, 6, 7, 2, 8, 4, 1],
       [6, 1, 2, 4, 3, 8, 7, 5, 9],
       [9, 2, 8, 7, 1, 5, 4, 6, 3],
       [3, 5, 7, 8, 4, 6, 1, 9, 2],
       [4, 6, 1, 9, 2, 3, 5, 8, 7],
       [8, 7, 6, 3, 9, 4, 2, 1, 5],
       [2, 4, 3, 5, 6, 1, 9, 7, 8],
       [1, 9, 5, 2, 8, 7, 6, 3, 4]]

sud2 = [[5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5, 5]]


sud3 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]]
# sum of each rwo should = 45
# the frequency of each number should be no greater 1

# sum of each column should be 45
# frequency of each number should be no greater than 1


counts = [sud.count(num) for num in sud]
all_counts = all([[arr.count(num) == 1 and num > 0 for num in arr]
                 for arr in sud2])
# print(all_counts)


def create_boxes(board):

    rows = [[num for num in arr] for arr in board]

    boxes = []

    c = 3
    start = 0

    while c < 10:

        r = 0

        while r < 9:
            box = rows[r][start:c] + rows[r+1][start:c] + rows[r+2][start:c]
            boxes.append(box)
            r += 3

        c += 3
        start += 3

    return boxes


def validate_sudoku(board):

    rows_check = all([all([arr.count(num) == 1 and num > 0 for num in arr])
                      for arr in board])
    cols_check = all([all([arr.count(num) == 1 and num > 0 for num in list(arr)])
                      for arr in zip(*board)])
    boxes_check = all(
        all([arr.count(num) == 1 and num > 0 for num in arr]) for arr in create_boxes(board))

    return all([rows_check, cols_check, boxes_check])

    # return valid


# print(create_boxes(sud))

print(validate_sudoku(sud))

# vals = [False, False, False]

# print(all(vals))

# an array of false booleans is still truthy
# so all([False, False, False]) evaluates to True


list = [1, 2, 3]
myset = {1, 2, 3}

# print(set(list)=myset)


#   if elements != {(board[q][w]) for w in range(j-3, j) for q in range(i-3, i)}:
