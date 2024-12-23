"""

Python Advanced - Meta Class
Keyword - Type(name, base, dct), Dynamic metaclass

"""
"""

메타클래스
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점

"""

# Ex1
# type 동적 클래스 생성 예제

# Name(이름), Bases(상속), Dct(속성, 메소드)
s1 = type('Sample1', (), {})  # class sample1 으로 생성한것과 동일함.
# 차례대로 name, bases, dct임. name 은 Sample1, bases는 튜플 ()로, Dct는 {}로
'''

class Sample():
    pass

'''

print('Ex1 > ', s1)
print('Ex1 > ', type(s1))
print('Ex1 > ', s1.__base__)
print('Ex1 > ', s1.__dict__)

# 동적 생성 + 상속
class Parent1:
    pass
'''
class Sample2(Parent1):
    attr1 = 100
    attr2 = 'hi'
'''
#위와 같음.
s2 = type(
        'Sample2', 
        (Parent1,), 
        dict(attr1=100, attr2='hi')
    ) #dict 말고 {'attr1':100, 'attr2':'hi'}라고 해도됨.

print('Ex2 > ', s2)
print('Ex2 > ', type(s2))
print('Ex2 > ', s2.__base__)
print('Ex2 > ', s2.__dict__)
print('Ex2 > ', s2.attr1, s2.attr2)
#프린트 결과
'''
Ex2 >  <class '__main__.Sample2'>
Ex2 >  <class 'type'>
Ex2 >  <class '__main__.Parent1'>
Ex2 >  {'attr1': 100, 'attr2': 'hi', '__module__': '__main__', '__doc__': None}
Ex2 >  100 hi
'''

print()

# Ex2
# type 동적 클래스 생성 + 메소드

class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n
    
    def mul(self, m, n):
        return m * n
    
ex = SampleEx()

print('Ex2 > ', ex.attr1)
print('Ex2 > ', ex.attr2)
print('Ex2 > ', ex.add(100,200))
print('Ex2 > ', ex.mul(100,20))

'''
Ex2 >  30
Ex2 >  100
Ex2 >  300
Ex2 >  2000
'''

print()

s3 = type(
        'Sample3', 
        (object, ), 
        dict(attr1=30, attr2=100, add=lambda x, y:x+y, mul=lambda x, y: x*y)
    )   # 빈 괄호로 써도되고 object라고 써도됨.

print('Ex2 > ', s3.attr1)
print('Ex2 > ', s3.attr2)
print('Ex2 > ', s3.add(100,200))
print('Ex2 > ', s3.mul(100,20))

'''
Ex2 >  30
Ex2 >  100
Ex2 >  300
Ex2 >  2000
'''
#class로 직접 선언한 위의 ex 와 동적으로 작성한 s3가 결과가 같은것을 알 수 있음.
