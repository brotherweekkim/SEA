n = int(input())
for test in range(1,n+1):
    num1,num2 = map(int,input().split())
    print(f'#{test}', end=' ')
    if num1 < num2:
        print("<")
    elif num1 > num2:
        print(">")
    else :
        print("=")