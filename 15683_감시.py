# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cctv_dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
    ]

# 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어짐
# 0은 빈 칸, 6은 벽, 1~5는 CCTV
# 1번 CCTV는 한 쪽 방향만 감시 가능
# 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향
# 4번은 세 방향
# 5번은 네 방향
# CCTV의 최대 개수는 8개를 넘지 않는다.

# 세로의 크기 N과 가로의 크기 M
N, M = list(map(int, input().split()))
# 사무실
office = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
ans = float("inf")
cctv_spot = []
cctv_cnt = 0

for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv_cnt += 1
            cctv_spot.append([i, j, office[i][j]])

def dfs(t):
    global cctv_cnt, ans
    ans_cnt = 0
    if t == cctv_cnt:
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    ans_cnt += 1
        ans = min(ans, ans_cnt)
        return

    cctv_dx = cctv_spot[t][0]  # cctv의 x좌표
    cctv_dy = cctv_spot[t][1]  # cctv의 y좌표
    cctv_type = cctv_spot[t][2]  # cctv의 타입(번호) range 1 ~ 5

    for dir in cctv_dir[cctv_type]:
        reset = [] # deepcopy를 사용하지 않기 위해 원래상태로 복구할 좌표를 담을 list
        for d in dir: # 각 타입의 모든 방향으로 탐색
            ax = cctv_dx
            ay = cctv_dy
            while True:
                ax += dx[d]
                ay += dy[d]
                if 0 <= ax < N and 0 <= ay < M and office[ax][ay] != 6: # 벽이 아니고 사무실을 벗어나지 않을 때
                    reset.append([ax, ay, office[ax][ay]]) # board를 원상복구시키기 위한 배열에 삽입
                    office[ax][ay] = 7
                else:
                    break
        dfs(t+1) # 다음 cctv 좌표 확인
        for x, y, type in reset: # 탐색한 좌표들을 다시 원상복구해야 다음번 탐색이 독릭접으로 실행될 수 있음
            office[x][y] = type

dfs(0)
print(ans)