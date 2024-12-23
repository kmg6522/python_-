"""

컨텍스트 매니저 : 원하는 타이밍 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)

"""

# Ex1

file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1.')
finally:
    file.close()    #write내용이 파일에 써지는것 확인 가능


# Ex2

with open('.testfile2.txt', 'w') as f:     #with 문으로 위의 Ex1을 그대로 구현가능
    f.write('Context Manager Test1\nContextlib Test1.')

# Ex3
# Use Class -> Context Manager with exception handling.

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self):   #진입하는 매쏘드
        print('MyFileWriter started : __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, value, trace_back):  #끝날때 발동되는 매쏘드
        print('MyFileWriter started : __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter('./testfile5.txt', 'w') as f:
    raise ValueError("Error")
    #f.write('Context Manager Test3\nContextlib Test3.')
