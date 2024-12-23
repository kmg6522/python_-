"""

Python Advanced - Property - Getter, Setter
Keywork - @Property

"""

"""

프로버티(Property) 사용 장점
1. 파이써닉한 코드
2. 변수 제약 설정
3. Getter, Setter 효과 동등(코드일관성)
     - 캡슐화-유효성 검사 가능 추가 용이
     - 대체 표현(속성 노출, 내부의 표현 숨기기 가능)
     - 속성의 수명 및 메모리 관리 용이
     - 디버깅 용이
     - Getter, Setter 작동에 대해 설계된 여러 라이브러리(오픈소스) 상호 운용성 증가

"""

# Ex1
# Property 활용 Getter, Setter 작성

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0 #private

    @property
    def y(self):  #getter
        print('Called get method')  #실행되는건지 확인위해 프린트.
        return self.__y
    
    @y.setter   #setter    # 내부적으로 모두 def y 지만 property 선언에 따라 작동이 달라지는것. 
    def y(self, value):
        print('Called set method')
        self.__y = value

    @y.deleter   # 내부적으로 모두 def y 지만 property 선언에 따라 작동이 달라지는것. 
    def y(self):
        print('Called delete method')
        del self.__y
    
a = SampleA()

a.x = 1
a.y = 2   #이걸 명령함으로써 called set method가 출력됨.

print('Ex1 > x: {}'.format(a.x))
print('Ex1 > y: {}'.format(a.y))   #이걸 가져올땐 called get method가 프린트됨.

#따라서 위의 결과는 아래와 같이 출력됨.
'''
Called set method
Ex1 > x: 1
Called get method
Ex1 > y: 2
'''

# Deleter
# del a.y a_SampleA_y -> 딱 이 변수에 해당하는거만 지우고싶을때 사용
# print('Ex1 > ', dir(a))

# Ex2

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 #private

    @property
    def y(self):  #getter
        print('Called get method')  #실행되는건지 확인위해 프린트.
        return self.__y
    
    @y.setter   #setter    # 내부적으로 모두 def y 지만 property 선언에 따라 작동이 달라지는것. 
    def y(self, value):
        print('Called set method')
        if value < 0:
            raise ValueError('0보다 큰 값을 입력하세요.')
        self.__y = value

    @y.deleter   # 내부적으로 모두 def y 지만 property 선언에 따라 작동이 달라지는것. 
    def y(self):
        print('Called delete method')
        del self.__y

b = SampleB()

b.x = 1
b.y = 10

# b.y = -5 #예외발생 -> value가 0보다 작으면 에러나게끔 설정되있으므로.

print('Ex2 > x: {}'.format(b.x))  #1
print('Ex2 > y: {}'.format(b.y))  #10




