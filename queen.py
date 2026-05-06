def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([r[:] for r in board])
            return
        
        for col in range(n):
            if cols[col] or diag1[row - col + n - 1] or diag2[row + col]:
                continue
            
            board[row][col] = "Q"
            cols[col] = True
            diag1[row - col + n - 1] = True
            diag2[row + col] = True
            
            backtrack(row + 1)
            
            board[row][col] = "."
            cols[col] = False
            diag1[row - col + n - 1] = False
            diag2[row + col] = False

    backtrack(0)
    return solutions


# Function to print nicely
def print_board(board, num):
    print(f"\nSolution {num}:")
    n = len(board)
    
    for row in board:
        print("+---" * n + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * n + "+")


# ---- Driver ----
n = int(input("Enter value of N: "))
solutions = solve_n_queens(n)

print(f"\nTotal Solutions: {len(solutions)}")

for i, sol in enumerate(solutions, 1):
    print_board(sol, i)