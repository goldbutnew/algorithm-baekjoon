my_bingo = [list(map(int, input().split())) for _ in range(5)]

arr = [list(map(int, input().split())) for _ in range(5)]

# 1차원 배열로 변경
mc_bingo = []
for element in arr:
    mc_bingo += element

# 빙고 확인
def check_bingo(my_bingo):

    bingo_cnt = 0

    # 행 탐색
    for i in range(5):
        row_total = 0
        for j in range(5):
            row_total += my_bingo[i][j]
        if row_total == 0:
            bingo_cnt += 1

    # 열 탐색
    for j in range(5):
        col_total = 0
        for i in range(5):
            col_total += my_bingo[i][j]
        if col_total == 0:
            bingo_cnt += 1

    # 대각선 탐색
    # \ 방향의 합
    rd_total = 0
    for i in range(5):
        rd_total += my_bingo[i][i]
    if rd_total == 0:
        bingo_cnt += 1

    # / 방향 합
    ld_total = 0
    for i in range(5):
        ld_total += my_bingo[i][4-i]
    if ld_total == 0:
        bingo_cnt += 1

    return bingo_cnt


# 게임 시작
cnt = 0
for k in range(25):
    for i in range(5):
        for j in range(5):
            if mc_bingo[k] == my_bingo[i][j]:
                my_bingo[i][j] = 0
                cnt += 1
                # print(cnt)
                exit()

            if cnt >= 12:
                if check_bingo(my_bingo) >= 3:
                    ans = k+1
                    print(ans)

print(cnt)