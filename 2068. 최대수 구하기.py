n = int(input())
for test in range(1,n+1):
    num_list = list(map(int,input().split()))
    print(f'#{test} {max(num_list)}')