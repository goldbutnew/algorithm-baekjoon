from collections import deque

# 회전 초밥 벨트에 놓인 접시수 N
# 초밥의 가짓수 d
# 연속해서 먹는 접시의 수 k
# 쿠폰 번호 c
# 2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d

N, d, k, c = map(int, input().split())

belt = deque()

# 1~d 사이의 숫자가 N개의 줄에 걸쳐 주어짐
for _ in range(N):
    sushi = int(input())
    belt.append(sushi)

# 초기값 설정
ans = 0

# N번 동안 한 칸씩 회전
for _ in range(N):
    # 임시 빈 리스트 생성
    t_lst = []
    # k 만큼 델타 탐색하며 먹은 스시 t_lst에 저장
    for di in range(k):
        t_lst.append(belt[di])
    # 보너스 스시 저장
    t_lst.append(c)
    # set으로 중복 제거
    if len(set(t_lst)) > ans:
        # ans보다 len(set(t_lst))가 크다면 ans 값 갱신
        ans = len(set(t_lst))
    # 회전 초밥 돌리기
    belt.rotate(1)

print(ans)