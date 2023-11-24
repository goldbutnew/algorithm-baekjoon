n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 가로: dp[x][y][0]
# 세로: dp[x][y][1]
# 대각선: dp[x][y][2]

# 맨 윗줄은 계속 가로로만 놓을 수 있음
dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if home[i][j - 1] != 1:
            dp[i][j][0] += dp[i][j - 1][0]
            if i > 0:
                dp[i][j][0] += dp[i][j - 1][2]
        if home[i - 1][j] != 1:
            dp[i][j][1] += dp[i - 1][j][1]
            if i > 0:
                dp[i][j][1] += dp[i - 1][j][2]
        if i > 0 and not home[i][j - 1] + home[i - 1][j] + home[i - 1][j - 1]:
            dp[i][j][2] += sum(dp[i - 1][j - 1])

print(sum(dp[-1][-1]) if home[-1][-1] != 1 else 0)