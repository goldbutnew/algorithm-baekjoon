t = int(input())

# n은 10000보다 작거나 같으니까 dp의 길이를 10001로 설정
# 숫자 1만 사용하는 경우의 수를 모든 n이 1개씩 보유하고 있으므로 1로 초기화
dp = [1] * 10001

# 2가 들어가는 경우
for i in range(2, 10001):
    dp[i] += dp[i - 2]

# 3이 들어가는 경우
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])