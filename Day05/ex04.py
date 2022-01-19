
# 논리연산자
# and   :   A and B  와 같은 조건에서, 
#           A와 B 모두 True(참)일 때, 결과 True(참)이다.

# or    :   A or B  와 같은 조건에서, 
#           A와 B 둘 중 하나의 조건이라도 True(참)이면, 결과 True(참)이다.

# not   :   True 이면, False 로, False 이면, True 로 변경한다.
a = 10
b = 5

print('{} > 7 and {} > 7 : {}'.format(a, b, a > 7 and b > 7))
print('{} > 7 or {} > 7 : {}'.format(a, b, a > 7 or b > 7))

print('not {} : {}'.format(a, not a))
print('not {} : {}'.format(0, not 0))

