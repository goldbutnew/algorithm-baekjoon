n = int(input())

if n % 3 == 2 or n % 3 == 0:
    if (n // 3) % 2 == 1:
        print("SK")
    elif (n // 3) % 2 == 0:
        print("CY")

elif n % 3 == 1:
    if (n // 3) % 2 == 1:
        print("CY")
    elif (n // 3) % 2 == 0:
        print("SK")