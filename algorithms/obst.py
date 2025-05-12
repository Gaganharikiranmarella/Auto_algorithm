def obst(keys, freq):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
    for L in range(2, n+1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')
            total_freq = sum(freq[i:j+1])
            for r in range(i, j+1):
                c = (0 if r == i else cost[i][r-1]) + \
                    (0 if r == j else cost[r+1][j]) + total_freq
                cost[i][j] = min(cost[i][j], c)
    return cost[0][n-1]
