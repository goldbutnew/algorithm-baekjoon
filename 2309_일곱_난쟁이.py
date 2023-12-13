from itertools import permutations

# 난쟁이 일곱 명 키의 합은 100

height_lst =[]

for _ in range(9):
    n = int(input())
    height_lst.append(n)

find_comb = list(permutations(height_lst, 7))

for comb in find_comb:
    if sum(comb) == 100:
        ans = comb
        break
    else:
        continue

ans = list(ans)
ans.sort()

for a in ans:
    print(a)