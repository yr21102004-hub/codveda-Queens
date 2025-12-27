class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n     # board[row] = column
        self.solutions = []

    def is_safe(self, current_row, column):
        """
        Check if placing a queen at (current_row, column) is safe
        """
        for previous_row in range(current_row):
            # Same column check
            if self.board[previous_row] == column:
                return False

            # Diagonal check
            if abs(self.board[previous_row] - column) == abs(previous_row - current_row):
                return False
        return True

    def solve(self, row=0):
        """
        Solve the N-Queens problem using backtracking
        """
        # If all queens are placed, store the solution
        if row == self.n:
            self.solutions.append(self.board.copy())
            return

        # Try placing queen in each column
        for column in range(self.n):
            if self.is_safe(row, column):
                self.board[row] = column     # Place queen
                self.solve(row + 1)          # Move to next row
                self.board[row] = -1         # Backtrack

    def get_solutions(self):
        """
        Return all valid solutions
        """
        self.solve()
        return self.solutions

    def print_solutions(self):
        """
        Print solutions in board format
        """
        for solution in self.solutions:
            for row in range(self.n):
                line = ""
                for col in range(self.n):
                    if solution[row] == col:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print("-" * 20)