from Queen import NQueens

n = int(input("Enter number of queens: "))

n_queens = NQueens(n)
solutions = n_queens.get_solutions()

print(f"\nTotal solutions: {len(solutions)}\n")
n_queens.print_solutions()