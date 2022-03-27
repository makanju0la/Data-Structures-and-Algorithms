# Validate Sudoku

def isValidSudoku(self, board):
    for i in range(len(board)):
        rowSet = set()
        for j in range(len(board[0])):
            if board[i][j] != '.':
                if board[i][j] not in rowSet:
                    rowSet.add(board[i][j])
                else:
                    return False
    for i in range(len(board)):
        colSet = set()
        for j in range(len(board[0])):
            if board[j][i] != '.':
                if board[j][i] not in colSet:
                    colSet.add(board[j][i])
                else:
                    return False
    boxes = [set() for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '.':
                index = (i // 3) * 3 + j // 3  # Gives us index from 0-8
                if board[i][j] not in boxes[index]:
                    boxes[index].add(board[i][j])
                else:
                    return False
    return True