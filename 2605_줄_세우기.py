N = int(input())
numbers = list(map(int, input().split()))

ans_lst = []

ans_lst.append(numbers[0]+1)

for i in range(1, N):
    t = numbers[i]
    ans_lst.insert(i-t, i+1)

print(*ans_lst)