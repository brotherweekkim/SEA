n = int(input())
for test in range(1,n+1):
    number_list = list(map(int,input().split()))
    total = sum(number_list)
    length = len(number_list)
    print(f'#{test} {round(total/length)}') # 반올림 할 때는 round 함수