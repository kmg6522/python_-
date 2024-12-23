"""

객체의 복사 종류 : Copy, Shallow Copy, Deep Copy
정확한 이해 후사용 -> 프로그래밍 개발 중요(문제 발생 요소)
가변 : list, set, dict

"""

# Ex1 - Copy

a_list = [1,2,3,[4,5,6],[7,8,9]]
b_list = a_list

print('Ex1 > ', id(a_list))
print('Ex1 > ', id(b_list))

b_list[2] = 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)

b_list[3][2] = 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)     #b_list를 바꿔도 a_list까지 모두 바뀌는 것을 알 수 있음.


# Ex2 - Shallow Copy
import copy

c_list = [1,2,3,[4,5,6],[7,8,9]]
d_list = copy.copy(c_list)

print('Ex2 > ', id(c_list))
print('Ex2 > ', id(d_list))

d_list[1] = 100

print('Ex2 > ', c_list)
print('Ex2 > ', d_list)

d_list[3].append(1000)
d_list[4][1] = 10000

print('Ex2 > ', c_list)
print('Ex2 > ', d_list)     #d_list만 변경하였는데도 c_list까지도 1000과 10000이 추가되었음. 이는 리스트 안의 리스트에 대해 값을 변경했기 때문이고, shallow copy에서는 이렇게 작동함.


# Ex3 - Deep Copy

e_list = [1,2,3,[4,5,6],[7,8,9]]
f_list = copy.deepcopy(e_list)

print('Ex3 > ', id(e_list))
print('Ex3 > ', id(f_list))

f_list[3].append(1000)
f_list[4][1] = 10000

print('Ex3 > ', e_list)
print('Ex3 > ', f_list)    #f_list만 변경했기에 e_list에는 적용안된 것을 확인할 수 있음. deep copy이기 때문.
