T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = int(input())
    number_list = list(map(int,input().split()))
    print(f'#{test_case}',end= " ")
    max_idx = min_idx = 0
    for idx in range(number):
        if number_list[idx] >= number_list[max_idx]:
            max_idx = idx
        if number_list[idx] < number_list[min_idx]:
            min_idx = idx
    print(abs(max_idx-min_idx))