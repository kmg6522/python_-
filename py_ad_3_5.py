"""
Python Advanced - Descriptor
Keyword - descriptor vs property, low level(descriptor) vs high level(property)

"""

"""
디스크립터
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. Property와 달리 reuse(재사용) 가능
3. ORM Framework 사용
"""

# Ex1
# Descript 예제1

import os

class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname

#현재 경로
s=DirectoryPath('./')

print(s.size)

#헷갈릴 때 출력 용도
print('Ex1 > ', dir(DirectoryPath))  #dir 은 값까지 나타내진않음. 어떤 속성이 있는지만 나열해줌. '__class__', '__delattr__', '__dict__' 이런식. 
print('Ex1 > ', DirectoryPath.__dict__)    #클래스 속성으로 접근해야 모두 다 볼수있음. 'size': <__main__.DirectoryFileCount object at 0x7fc11001dfd0>를 통해 어디로 연결된건지 알 수 있음.
print('Ex1 > ', dir(s))
print('Ex1 > ', s.__dict__)



# Ex2
# Descriptor 예제(2)

import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value
    
    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value
    
    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value=value

class Student:
    # Descriptor instance
    score = LoggedScoreAccess()

    def __init__(self, name):
        # Regular instance attribute
        self.name = name

s1 = Student('Kim')
s2 = Student('Lee')

# 점수 확인(s1)
print('Ex2 > ', s1.score)
s1.score += 20
print('Ex2 > ', s1.score)

# 점수 확인(s2)
print('Ex2 > ', s2.score)
s1.score += 30
print('Ex2 > ', s2.score)     #s1, s2 모두 score가 중첩되서 반영됨. 코드 오류
