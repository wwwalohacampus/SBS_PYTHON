# 딕셔너리
# '사전' - (단어) : (뜻)
# - 키(key) : 값(value)을 한 쌍으로 구성한 컬렉션
# - 인덱스가 존재하지 않는다.
# - 기호 : { key : value }
# - dic = { 키1 : 값1, 키2 : 값2, ... }
# - 값1 = dic[키1]

d = { 'a': 'apple', 'b' : 'banana' }
print('d : ', d)

print('d[\'a\'] : ', d['a'])
print('d[\'b\'] : ', d['b'])


# 딕셔너리의 요소 추가
# : 새로운 키를 작성하여 값을 대입한다.
d['c'] = 'melon'
print('d : ', d)

# 다른 추가 방법
# : setdefault() 함수를 이용
d.setdefault('d', 'dog')
print('d : ', d)

# 딕셔너리 요소 수정
d.update(d='cat')
print('d : ', d)

# 딕셔너리 요소 삭제
d.pop('d')
print('d : ', d)