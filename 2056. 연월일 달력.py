n = int(input())
for test in range(1,n+1):
    date = input()
    print(f'#{test}', end=' ')
    # print(int(date[4:6]))
    if int(date[4:6]) == 0: print(-1)
    elif int(date[4:6]) == 2:
        if 1 <= int(date[6:]) <= 28:
            print(f'{date[:4]}/{date[4:6]}/{date[6:]}')
        else: print(-1)
    elif int(date[4:6]) == 1 or 3 or  5 or 7 or 8 or 10 or 12:
        if 1 <= int(date[6:]) <= 31:
            print(f'{date[:4]}/{date[4:6]}/{date[6:]}')
        else: print(-1)
    elif int(date[4:6]) == 4 or 6 or  9 or 11:
        if 1 <= int(date[6:]) <= 31:
            print(f'{date[:4]}/{date[4:6]}/{date[6:]}')
        else: print(-1)
    else: print(-1)

# 안되는 이상한 코드
n = int(input())
for test in range(1,n+1):
    date = input()
    print(f'#{test}', end=' ')
    # print(int(date[4:6]))
    # if int(date[4:6]) == 0: print(-1) 이 줄이 없으면 20220011이 2022/00/11로 출력됨 왜 일까?
    if int(date[4:6]) == 2:
        if 1 <= int(date[6:]) <= 28:
            print(f'{date[:4]}/{date[4:6]}/{date[6:]}')
        else: print(-1)
    elif int(date[4:6]) == 1 or 3 or  5 or 7 or 8 or 10 or 12:
        if 1 <= int(date[6:]) <= 31:
            print(f'{date[:4]}/{date[4:6]}/{date[6:]}')
        else: print(-1)
    elif int(date[4:6]) == 4 or 6 or  9 or 11:
        if 1 <= int(date[6:]) <= 31:
            print(f'{date[:4]}/{date[4:6]}/{date[6:]}')
        else: print(-1)
    else: print(-1)