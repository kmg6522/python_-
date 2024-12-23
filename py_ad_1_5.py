"""

Keyword - Contextlib, __enter__, __exit__

"""

# Ex1
# Use Class

import time

class ExcuteTimer(object):  #object 없어도됨
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} : {} s'.format(self._msg, time.monotonic() - self._start))
        return True
    
with ExcuteTimer('Start! job') as v:   
    print('Received start monotonic1 : {}'.format(v))   #여기서 v는 위에 self._start값을 출력함.

    # Excute job 
    for i in range(10000000):      #시간을 흐르게 하는 작업 임의로 설정
        pass

    #raise Exception('Raise! Exception!!') #강제로 예외 발생시키기. raise Exception을 하면 __exit__ 메서드가 호출되면서 exc_type이 True가 되는것.
    #발생시켜보면 Logging exception (<class 'Exception'>, Exception('Raise! Exception!!'), <traceback object at 0x7fee500f9140>) 이와 같이 나오는걸 알 수 있음.
