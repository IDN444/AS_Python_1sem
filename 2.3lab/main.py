def SwapCol(A, K1, K2):
    for i in range(len(A)):
        A[i][K1], A[i][K2] = A[i][K2], A[i][K1]
