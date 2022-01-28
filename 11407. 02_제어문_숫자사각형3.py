T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    b, c = map(int, input().split())
    print(f'#{test_case}')
    for i in range(1,b+1):
        for j in range(1,c):
            if i % 2:
                print((i-1)*c+j, end= ' ')
            else :
                print(i*c-j+1, end= ' ')
        if i % 2:
            print(i*c)
        else :
            print(i*c-b)
