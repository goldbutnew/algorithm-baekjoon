# 수학여행에 참가하는 학생 수 N, 한 방에 배정할 수 있는 최대 인원 수 K
N, K = map(int, input().split())

girl_cnt_lst = [0] * 6
boy_cnt_lst = [0] * 6

# 학생의 성별 S, 학년 Y
for _ in range(N):
    S, Y = map(int, input().split())

    # 여학생인 경우 0, 남학생인 경우 1
    if S == 0:
        girl_cnt_lst[Y-1] += 1
    elif S == 1:
        boy_cnt_lst[Y-1] += 1

# print(girl_cnt_lst)
# print(boy_cnt_lst)

# 방의 수 계산하기
cnt_room = 0

# 여학생
for i in girl_cnt_lst:
    t = i//K+1
    if i == 0:
        cnt_room += 0
    elif i > 0 and i % K != 0:
        cnt_room += t
    elif i > 0 and i % K == 0:
        cnt_room += (t-1)

# 남학생
for i in boy_cnt_lst:
    t = i//K+1
    if i == 0:
        cnt_room += 0
    elif i > 0 and i % K != 0:
        cnt_room += t
    elif i > 0 and i % K == 0:
        cnt_room += (t-1)

# print(girl_cnt_lst)
# print(boy_cnt_lst)

print(cnt_room)