N = 8
board = [[0] * N for i in range(N)]

def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        if col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False

    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False

board[0][0] = 1

if solve(1):
    for row in board:
        print(row)
else:
    print("No solution found")
