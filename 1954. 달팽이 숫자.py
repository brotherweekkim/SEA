def snail(number):
    if number == 1:
        return 1
    for i in range(1,number+1):
        print(i,end=' ')
    print(f'\n{(number-1)*4}',end=' ')
    print(f'{snail(number-2)+(number-1)*4}', end=' ')
    print(f'{number+1}')
    for i in range((number-1)*3+1,(number-1)*2,-1):
        print(i,end=' ')

T = int(input())
for test in range(1,T+1):
    num = int(input())
    snail(num)
# 포기...