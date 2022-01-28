T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    number_set = set(map(int,input().split()))
    number_list = list(number_set)
    print(f'#{test_case}',end= " ")
    number_list= sorted(number_list)
    print(number_list[K-1])