# 통과!
T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    numbers = list(map(int,input().split()))
    print(f'#{test_case}', end=' ')
    result = 0
    while len(numbers) > 1:
        max_number = numbers[0]
        max_index = 0
        for idx, number in enumerate(numbers):
            if max_number <= number:
                max_number = number
                max_index = idx
        if max_index == 0:
            numbers = numbers[max_index+1:]
            continue
        result += max_index * max_number - sum(numbers[:max_index])
        numbers = numbers[max_index+1:]
    print(result)

# 시간 초과
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    numbers = list(map(int,input().split()))
    print(f'#{test_case}', end=' ')
    # print((numbers[:0]))      # 빈리스트
    result = 0
    while len(numbers) > 1:        # numbers의 개수가 1개이면 그만한다.
        max_index = numbers.index(max(numbers))     # 최대값의 인덱스를 구한다.
        for number in numbers[:max_index]:          # 최대값 앞의 인자들을
            result += max(numbers)-number           # 최대값에 팔 예정이므로 최대값에서 산값을 빼준다.
        numbers = numbers[max_index+1:]             # 최대값 뒤에 리스트를 따로 뽑는다.
        # print(result)
    print(result)
'''
# 참고할만한 풀이, 뒤에서부터 접근
'''
num = int(input())
 
for i in range(num):
    n = int(input())
    data = list(map(int,input().split(" ")))
 
    benefit = 0
    maxi = 0
    for j in range(n-1,-1,-1):
        maxi = max(maxi,data[j])
        if data[j] < maxi:
            benefit+=maxi-data[j]
        else:
            pass
    print(f'#{i+1} {benefit}')
'''