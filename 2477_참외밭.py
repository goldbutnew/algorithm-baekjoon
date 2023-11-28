K = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4

max_garo = 0
max_garo_idx = 0
max_sero = 0
max_sero_idx = 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
       if arr[i][1] > max_garo:
           max_garo = arr[i][1]
           max_garo_idx = i
    else:
        if arr[i][1] > max_sero:
            max_sero = arr[i][1]
            max_sero_idx = i

max_s = max_garo * max_sero

# 최대값에서 빼 줄 범위 구하기
mini_sero = abs(arr[(max_sero_idx + 1) % 6][1] - arr[(max_sero_idx - 1) % 6][1])
mini_garo = abs(arr[(max_garo_idx + 1) % 6][1] - arr[(max_garo_idx - 1) % 6][1])

mini_s = mini_garo * mini_sero

s = max_s - mini_s

ans = s * K

print(ans)