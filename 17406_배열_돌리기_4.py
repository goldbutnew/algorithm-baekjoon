from copy import deepcopy
from itertools import permutations

# 배열의 크기 N, M
# 회전 연산의 개수 K
N, M, K = map(int, input().split())

# 배열 A
A = [list(map(int, input().split())) for _ in range(N)]

# 회전 연산의 정보 r, c, s
rcs = [list(map(int, input().split())) for _ in range(K)]

ans = 5000

# rcs 배열에서 회전 수 k 만큼 순열 생성
for p in permutations(rcs, k):
    # 원본 깊은 복사
    copyA = deepcopy(A)
    # 회전
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copyA[r-n][c+n]
            # 오른쪽
            copyA[r-n][c-n+1:c+n+1] = copyA[r-n][c-n:c+n]
            # 위쪽
            for row in range(r-n, r+n):
                copyA[row][c-n] = copyA[row+1][c-n]
            # 왼쪽
            copyA[r+n][c-n:c+n] = copyA[r+n][c-n+1:c+n+1]
            # 아래쪽
            for row in range(r+n, r-n, -1):
                copyA[row][c+n] = copyA[row-1][c+n]
            copyA[r-n+1][c+n] = tmp

    # 최소값 찾기
    for row in copyA:
        ans = min(ans, sum(row))

print(ans)