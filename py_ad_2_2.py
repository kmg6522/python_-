"""

Python Advanced - Property(1) - Underscore
Keyword - access modifier(접근지정자), underscore

"""
"""

다양한 언더스코어 활용
파이썬 접근지정자 설명

"""

# Ex1
# Use underscore
# 1. 인터프리터, 2. 값 무시, 3. 네이밍(구체화, 자릿수)

# Unpacking
x, _, y = (1, 2, 3)

a, *_, b = (1, 2, 3, 4, 5)

print('Ex1 > ', x, y, a, b)    # 1 3 1 5

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass

# Ex2
# 접근지정자
# name : public
# _name : protected
# __name : private
# 파이썬 -> Public 강제X, 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 정리 안함) -> Naming Mangling
# 타 클래스 __ 접근하지 않는 것이 원칙

# No use Property

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0

a = SampleA()

a.x = 1

print('Ex2 > x : {}'.format(a.x))

#print('Ex2 > x : {}'.format(a.__y)) # 에러남. 다른 naming mangling을 통해 다른 변수이름으로 내부적으로 바뀜.

print('Ex2 > ', dir(a))

print('Ex2 > z : {}'.format(a._z)) #private은 아니므로 출력됨. 그러나 외부에서 변경하지 않도록 권장됨. 암묵적 약속.

print('Ex2 > y : {}'.format(a._SampleA__y)) #굳이 출력하고자 하면 이와 같이 private 변수를 불러올 수 있음. 물론 자유도가 있기에 해당 변수 네이밍으로 값을 변경할 수도 있음. 그러나 권장하지 않음.

# Ex3
# 메소드 활용 Getter, Setter

class SampleB:   #private 변수에 대해 변경을 원한다면 아래와 같은 방식으로 함수를 지정해주어 접근해야함.
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y
    
    def set_y(self, value):
        self.__y = value

b = SampleB()

b.x = 1
b.set_y(2)

print('Ex3 > x : {}'.format(b.x))   #1
print('Ex3 > y : {}'.format(b.get_y()))   #set_y(2)로 인해 변경되어 get_y를 통해 2의 값을 출력함.

print('Ex3 > ', dir(b))


