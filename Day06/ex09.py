
# 대한민국의 수도를 맞추는 퀴즈

# 무한반복
# : 무조건 계속 반복하는 반복문
#   반드시, 종료조건을 넣어주어야 한다.
# break
# : 현재 속한 반복문을 벗어나는 키워드
while True:
    city = input('대한민국의 수도는 ?')
    # 종료조건
    if city == '서울' or city == 'seoul':
        print('정답입니다.')
        break
    else:
        print('틀렸습니다.')    