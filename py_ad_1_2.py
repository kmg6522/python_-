# Lambda, Reduce, Map, Filter Functions

"""
lambda 장점 : 익명, 힘 영역 사용 즉시 소멸, pythonic?, 파이썬 가비지 컬렉션(Count=0)
일반함수 : 새사용성 위해 메모리 저장
시퀸스형 전처리에 Reduce, Map, Filter 주로 사용
lambda, map, filter, reduce 설명 하기
"""

"""
lambda 관련 설명 !
lambda의 사용 예제
1. 간단한 계산
square = lambda x: x ** 2
print(square(4))  # 출력: 16

2. 조건부 표현식
max_value = lambda x, y: x if x > y else y
print(max_value(5, 8))  # 출력: 8

3. map과 함께 사용
lambda는 map과 같은 함수형 프로그래밍에서 자주 사용됩니다.

numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 출력: [1, 4, 9, 16]

4. filter와 함께 사용
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # 출력: [2, 4]

5. sort의 key 파라미터로 사용
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # 출력: [(1, 'one'), (3, 'three'), (2, 'two')]

"""
pairs = [(3, 'three'),(1, 'one'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)  # 출력: [(1, 'one'), (3, 'three'), (2, 'two')]

# Ex1
cul = lambda a, b, c: a*b+c

print('Ex1 > ', cul(10, 15, 20))

# Ex2
digits1 = [x * 10 for x in range(1, 11)]
print('Ex2 > ', digits1)

result = list(map(lambda i:i ** 2, digits1))  # digits1에서 인자 받음.

print('Ex2 > ', result)

def also_square(nums):
    def double(x):
        return x**2
    return map(double, nums)

print('Ex2 > ', list(also_square(digits1)))

# Ex3
digits2 = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda x:x % 2 ==0, digits2))

print('Ex3 > ', result)

def also_evens(nums):
    def is_even(x):
        return x%2==0
    return filter(is_even, nums)

print('Ex3 > ', list(also_evens(digits2)))


# Ex4
from functools import reduce

digits3 = [x for x in range(1, 101)]

result = reduce(lambda x, y : x+y, digits3)

print('Ex4 > ', result)

def also_add(nums):
    def add_plus(x, y):
        return x+y
    return reduce(add_plus, nums)

print('Ex4 > ', also_add(digits3))
