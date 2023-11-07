# 바이러스 확산
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < m :
            if t_lst[nx][ny] == 0:
                t_lst[nx][ny] = 2
                virus(nx,ny)

# 현재 안전 영역
def safezone():
    t_cnt = 0
    for i in range(n):
        for j in range(m):
            if t_lst[i][j] == 0:
                t_cnt += 1
    return t_cnt

# dfs
def dfs(wall):
    global ans

    if wall == 3:
        for i in range(n):
            for j in range(m):
                t_lst[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if t_lst[i][j] == 2:
                    virus(i,j)
        ans = max(ans, safezone())
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall += 1
                dfs(wall)
                lab[i][j] = 0
                wall -= 1

n, m = map(int,input().split())

# 0: 빈칸
# 1: 벽
# 2: 바이러스
lab = [list(map(int, input().split())) for _ in range(n)]

t_lst = [[0] * m for _ in range(n)]

# 델타 선언
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

dfs(0)

print(ans)