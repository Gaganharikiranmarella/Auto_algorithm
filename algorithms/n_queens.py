def n_queens(n):
    solutions = []
    def solve(queens, xy_diff, xy_sum):
        p = len(queens)
        if p == n:
            solutions.append(queens)
            return
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                solve(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
    solve([], [], [])
    return solutions
