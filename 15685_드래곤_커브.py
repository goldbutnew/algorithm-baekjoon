dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

empty_arr = [[0] * 101 for _ in range(101)]

# 드래곤 커브의 개수 정수 N
N = int(input())

for _ in range(N):
    # 드래곤 커브의 정보
    x, y, d, g = map(int, input().split())
    empty_arr[x][y] = 1
    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1] + 1) % 4)
        move.extend(tmp)
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        empty_arr[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if empty_arr[i][j]:
            if empty_arr[i+1][j] and empty_arr[i][j+1] and empty_arr[i+1][j+1]:
                ans += 1

print(ans)