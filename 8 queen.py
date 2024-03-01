def is_safe(board, row, col):
    # Check if there is a queen in the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queen_util(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queen_util(board, col + 1):
                return True

            board[i][col] = 0

    return False


def solve_queen():
    board = [[0] * 8 for _ in range(8)]

    if not solve_queen_util(board, 0):
        print("Solution does not exist")
        return False

    print("Solution:")
    for row in board:
        print(row)
    return True


if __name__ == "__main__":
    solve_queen()
