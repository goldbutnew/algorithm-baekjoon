r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
up = 0
down = 0

# 공기 청정기 위치
# 항상 1번 열에 설치되어 있으며 크기는 두 행을 차지
for i in range(r):
    if room[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                value = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        temp[nx][ny] += room[i][j] // 5
                        value += room[i][j] // 5
                room[i][j] -= value
    for i in range(r):
        for j in range(c):
            room[i][j] += temp[i][j]

# 위쪽 공기청정기 동작
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == up and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            dir += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

# 아래쪽 공기청정기 동작
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == down and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            dir += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

for _ in range(t):
    spread()
    air_up()
    air_down()

ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            ans += room[i][j]

print(ans)