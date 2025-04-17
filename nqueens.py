def solve_n_queens(n):
    result = []
    board = [["."] * n for _ in range(n)]

    def is_safe(r, c):
        for i in range(r):
            if board[i][c] == "Q":
                return False
            if c - (r - i) >= 0 and board[i][c - (r - i)] == "Q":
                return False
            if c + (r - i) < n and board[i][c + (r - i)] == "Q":
                return False
        return True

    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in board])
            return
        for c in range(n):
            if is_safe(r, c):
                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."

    backtrack(0)
    return result

# Test
queens = solve_n_queens(4)
for solution in queens:
    for row in solution:
        print(row)
    print()
