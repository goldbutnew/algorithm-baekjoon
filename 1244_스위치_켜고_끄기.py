switch_num = int(input())
switch_arr = list(map(int, input().split()))
student_num = int(input())
student_info = [list(map(int, input().split())) for _ in range(student_num)]

for i in range(student_num):

    if student_info[i][0] == 1:
        my_num = student_info[i][1]
        for k in range(len(switch_arr)):
            idx = my_num * (k+1) - 1
            if 0 <= idx < len(switch_arr):
                if switch_arr[idx] == 0:
                    switch_arr[idx] = 1
                else:
                    switch_arr[idx] = 0

    elif student_info[i][0] == 2:
        my_num = student_info[i][1]
        idx = my_num - 1
        if switch_arr[idx] == 0:
            switch_arr[idx] = 1
        elif switch_arr[idx] == 1:
            switch_arr[idx] = 0
        for k in range(1, len(switch_arr)):
            if 0 <= idx-k < len(switch_arr) and 0 <= idx+k < len(switch_arr):
                if switch_arr[idx-k] == switch_arr[idx+k]:
                    if switch_arr[idx-k] == 0 and switch_arr[idx+k] == 0:
                        switch_arr[idx-k] = 1
                        switch_arr[idx+k] = 1
                    elif switch_arr[idx-k] == 1 and switch_arr[idx+k] == 1:
                        switch_arr[idx-k] = 0
                        switch_arr[idx+k] = 0
                else:
                    break

for i in range(0, len(switch_arr), 20):
    print(* switch_arr[i:i+20])