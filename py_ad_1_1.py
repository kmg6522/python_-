"""

전역변수는 주로 변하지 않는 고정 값에 사용
지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시
전역 변수를 지역내에서 수정되는 것은 권장X

"""



# Ex1
a = 10 #Global variable

def foo():
    # Read global variable
    print('Ex1 > ', a)

foo()

# Read global variable
print('Ex1 > ', a)


# Ex2
b = 20

def bar():
    b = 30   # Local variable
    print('Ex2 > ', b)  # Read local variable

bar()
print('Ex2 > ', b)


# Ex3
c = 40

def foobar():
    #c = c + 10 # unbound local error
    #c += 100

    print('Ex3 > ', c)

foobar()

# Ex4
d = 50

def barfoo():
    global d
    d = 60
    d += 100
    print('Ex4 > ', d)

barfoo()

print('Ex4 > ', d)    # 위의 barfoo()를 실행함으로써 d가 전역변수가 됐으므로 160이 반영됨



# Ex5 (중요)

def outer():
    e = 70
    def inner():
        nonlocal e # inner함수의 지역변수가 아닌 outer에 존재하는 지역변수 e를 활용해주기 위함.
        e += 10
        print('Ex5 > ', e)
    return inner

in_test = outer()   # closure
in_test()
in_test()
in_test()

# Ex6
def func(var):
    x = 10
    def printer():
        print('Ex6 > ', "Printer Func Inner")
    print('Func Inner', locals())  # 지역 전체 출력

func('Hi')

# Ex7
print('Ex7 > ', globals()) # 전역 전체 출력
test_variables = 100
print('Ex7 > ', globals())

# Ex8(지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i,k)] = i + k

print('Ex8 >', plus_5_5)
print('Ex8 >', plus_9_9)
