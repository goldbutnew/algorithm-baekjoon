s = input()

# a의 숫자 카운팅
a = s.count('a')

# 원형으로 변경
s += s[0:a-1]

# 문자열의 길이는 최대 1,000
ans = 1000

# 기존 문자열의 길이 만큼의 포인터를 이동시키며
for i in range(len(s)-(a-1)):
	# i부터 i+a 사이에 b가 몇 개나 있는지 확인
    ans = min(ans, s[i:i+a].count('b'))

print(ans)