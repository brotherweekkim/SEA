num = int(input())
result = 0
while num%10 >= 1:  # 조건 주의하기 0.6789일때 나머지는 0.6789 몫은 0 But 6.789일때도 몫이 0 그냥 num//1이 자연수 일때라는 조건
    result += num%10
    num = num//10
print(result)