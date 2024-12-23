""""

with 구문 이해

"""

import contextlib
import time

# Ex1
# Use decorator

@contextlib.contextmanager    #contextlib 모듈에 포함된 데코레이터
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f  #__enter__
    f.close() #__exit__

with my_file_writer('testfile4.txt', 'w') as f:
    f.write('Context Manager Test4. \nContextlib Text4.')


# Ex2
# Use decorator

@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try:
        yield start
    except BaseException as e:
        print('Logging excpetion {} : {}'.format(msg,e))
        raise
    else: # __exit__     #try 블록이 성공적으로 실행되고, 예외가 발생하지 않았을 때 실행됨. 예외가 발생시 else 블록 실행되지 않음. 즉, try 블록이 제대로 수행되었을 경우에만 실행하고 싶은 코드를 작성.
        print('{} : {}s'.format(msg, time.monotonic() - start))

with ExcuteTimerDc('Start Job!') as v:
    print('Received start monotonic2 : {}'.format(v))   #start 값 출력한것
    # Excute job
    for i in range(10000000):
        pass
    #raise ValueError('occurred.')
