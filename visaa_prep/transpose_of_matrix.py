N=int(input().strip())
matrix=[input().strip().split() for _ in range(N)]
for j in range(N):
    print(" ".join(matrix[i][j] for i in range(N)))
