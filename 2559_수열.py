# 온도 측정한 전체 날짜의 수 N, K는 1과 N 사이의 정수
N, K = map(int, input().split())
# 측정한 온도를 나타내는 N개의 정수
arr = list(map(int, input().split()))

# 첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.

def prefix_sum(N, K):
    prefixSum = [0] * (N-K+1)
    prefixSum[0] = sum(arr[:K])
    for i in range(1, N):  # 두번째 값부터 누적합을 저장
        if 0 <= i + K - 1 < N:
            prefixSum[i] = prefixSum[i-1] - arr[i-1] + arr[i+K-1]
    return prefixSum

print(max(prefix_sum(N, K)))