T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    b, c = map(int, input().split())
    print(f'#{test_case}', end = ' ')
    idx = 1
    while b*idx <= c-b:
        print(b*idx, end= ' ')
        idx += 1
    print(b*idx)