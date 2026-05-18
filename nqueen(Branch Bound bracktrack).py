# N Queen Problem using Backtracking + Branch and Bound
N = 4

# Function to print board
def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# Recursive function
def solve(board, col,
          rows,
          upperDiagonal,
          lowerDiagonal):

    # Base Case
    if col >= N:
        return True

    # Try every row in current column
    for i in range(N):

        # Branch and Bound safety check
        if (rows[i] == False and
            lowerDiagonal[i + col] == False and
            upperDiagonal[N - 1 + col - i] == False):

            # Place queen
            board[i][col] = 1

            # Mark row and diagonals
            rows[i] = True
            lowerDiagonal[i + col] = True
            upperDiagonal[N - 1 + col - i] = True

            # Recursive call (Backtracking)
            if solve(board,
                     col + 1,
                     rows,
                     upperDiagonal,
                     lowerDiagonal):
                return True

            # Backtracking step
            board[i][col] = 0

            # Unmark row and diagonals
            rows[i] = False
            lowerDiagonal[i + col] = False
            upperDiagonal[N - 1 + col - i] = False

    return False


# Main function
def solveNQ():

    # Empty chessboard
    board = [[0 for i in range(N)]
             for j in range(N)]

    # Arrays for Branch and Bound
    rows = [False] * N
    upperDiagonal = [False] * (2 * N - 1)
    lowerDiagonal = [False] * (2 * N - 1)

    # Start solving from column 0
    if solve(board,
             0,
             rows,
             upperDiagonal,
             lowerDiagonal) == False:

        print("Solution does not exist")
        return False

    print("Solution Found:")
    printBoard(board)

    return True


# Driver Code
solveNQ()