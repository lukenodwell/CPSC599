def solve_recurrence():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    N = int(data[index])
    index += 1
    
    a = list(map(int, data[index:index + N + 1]))
    index += N + 1
    
    x = list(map(int, data[index:index + N]))
    index += N
    
    Q = int(data[index])
    index += 1
    
    queries = []
    for _ in range(Q):
        T = int(data[index])
        M = int(data[index + 1])
        queries.append((T, M))
        index += 2
    
    def matrix_mult(A, B, mod):
        return [[sum(x * y for x, y in zip(A_row, B_col)) % mod for B_col in zip(*B)] for A_row in A]
    
    def matrix_pow(mat, exp, mod):
        result = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))]
        base = mat
        while exp > 0:
            if exp % 2 == 1:
                result = matrix_mult(result, base, mod)
            base = matrix_mult(base, base, mod)
            exp //= 2
        return result
    
    def compute_xT(T, mod):
        if T < N:
            return x[T] % mod
        
        trans_mat = [[0] * N for _ in range(N)]
        for i in range(1, N):
            trans_mat[i - 1][i] = 1
        for j in range(N):
            trans_mat[N - 1][j] = a[N - j]

        trans_mat_pow = matrix_pow(trans_mat, T - N + 1, mod)

        result = sum(trans_mat_pow[N - 1][i] * x[N - 1 - i] for i in range(N)) % mod
        result = (result + a[0]) % mod
        return result
    
    results = []
    for T, M in queries:
        xT = compute_xT(T, M)
        results.append(xT)
    
    for result in results:
        print(result)

solve_recurrence()