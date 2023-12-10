light = list(input())

cnt = 0

for i in range(len(light)):
    if light[i] == 'Y':
        light[i] = 'N'
        for k in range(len(light)+1):
            k_idx = ((i+1) * k) -1
            if i < k_idx < len(light):
                if light[k_idx] == 'Y':
                    light[k_idx] = 'N'
                else:
                    light[k_idx] = 'Y'
        cnt += 1
    elif light[i] == 'N':
        pass

for l in light:
    if l == 'Y':
        cnt = -1
        break

print(cnt)