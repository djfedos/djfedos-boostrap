def isValidSudoku(board: list[list[str]]) -> bool:
    familiar_set = set()
    # first check rows:
    for row in board:
        for element in row:
            if element != '.':
                if element not in familiar_set:
                    familiar_set.add(element)
                else:
                    return False
        familiar_set.clear()
    # the check columns
    for column in range(9):
        for row in board:
            if row[column] != '.':
                if row[column] not in familiar_set:
                    familiar_set.add(row[column])
                else:
                    return False
        familiar_set.clear()
    # check the 3*3 squares
    square_sides = [(0, 3), (3, 6), (6, 9)]
    for y_side in square_sides:
        c, d = y_side
        for x_side in square_sides:
            a, b = x_side
            for x in range(a, b):
                for y in range(c, d):
                    if board[y][x] != '.':
                        if board[y][x] not in familiar_set:
                            familiar_set.add(board[y][x])
                        else:
                            return False
            familiar_set.clear()

    return True


if __name__ == '__main__':

    input_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(isValidSudoku(input_board))

    input_board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    print(isValidSudoku(input_board))


    input_board = [
         [".",".",".",".","5",".",".","1","."]
        ,[".","4",".","3",".",".",".",".","."]
        ,[".",".",".",".",".","3",".",".","1"]
        ,["8",".",".",".",".",".",".","2","."]
        ,[".",".","2",".","7",".",".",".","."]
        ,[".","1","5",".",".",".",".",".","."]
        ,[".",".",".",".",".","2",".",".","."]
        ,[".","2",".","9",".",".",".",".","."]
        ,[".",".","4",".",".",".",".",".","."]]

    print(isValidSudoku(input_board))
