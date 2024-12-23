"""

Python Advanced - Meta Class
Keyword - Type inheritance, Custom metaclass

"""

"""
메타클래스 상속
1. type클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기 가능(intercept)
    - 클래스 수정하기(modify)
    - 클래스 개선(기능추가)
    - 수정된 클래스 반환 

"""

# Ex1
# 커스텀 메타클래스 생성 예제 (Type 상속x)

def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

# list를 상속받음, 메소드 2개 추가

CustomList1 = type(
                'CustomList1', 
                (list,),
                {
                    'desc':'커스텀 리스트1',
                    'cus_mul':cus_mul, 
                    'cus_replace': cus_replace
                }
            )

c1 = CustomList1([1,2,3,4,5,6,7,8,9])   
#틀은 위에서 만들고 인스턴스화는 여기서 진행한것임. 
#위에 list를 상속받았기 때문에 구동된것. 
c1.cus_mul(1000)
c1.cus_replace(1000,7777)

print('Ex1 > ', c1)  #Ex1 >  [7777, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
print('Ex1 > ', c1.desc)
print('Ex1 > ', dir(c1))

# Ex2. 여기서부터는 딥한 개발이 들어가야 필요한 부분들임.
# 위의 type을 통해 생성한걸 내부적으로는 아래와 같이 작동된다를 보여주는것.
# 커스텀 메타클래스 생성 예제(Type 상속O)

# *args : *args는 임의의 수의 위치 인수를 튜플 형태로 받는 문법입니다. 이 문법을 사용하면 메서드나 함수가 입력받는 인수의 개수를 유연하게 처리할 수 있습니다.
# **kwargs : **kwargs는 임의의 수의 키워드 인수를 딕셔너리 형태로 받는 문법입니다. 이 문법을 사용하면 이름이 지정된 인수들을 유연하게 처리할 수 있습니다.


#실행순서는 new, init, call 순서임. type을 받았기때문에 init전에 new부터 시작.
class CustomListMeta(type):
    def __init__(self, object_or_name, bases, dict): #생성된 인스턴스 초기화
        print('__init__ -> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases,dict)

    def __call__(self, *args, **kwargs): #인스턴스 실행
        print('__call__ -> ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    def __new__(metacls, name, bases, namespace): #클래스 인스턴스 생성(메모리 초기화)
        print('__new__ -> ', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace

        return type.__new__(metacls, name, bases, namespace)
    
CustomList2 = CustomListMeta('CustomList2', (list,), {})

c2 = CustomList2([1,2,3,4,5,6,7,8,9])
c2.cus_mul(1000)
c2.cus_replace(1000,7777)

print('Ex2 > ', c2)
print('Ex2 > ', c2.desc)

# 상속 확인
print(CustomList2.__mro__) # (<class '__main__.CustomList2'>, <class 'list'>, <class 'object'>)
#CustomList2 는 list를, list는 object를 상속했다는 의미.

