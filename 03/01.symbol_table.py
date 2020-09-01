# global, local 심볼테이블 확인
g_a = 1
g_s = '마이콜'


def g_f():

    l_a = 2
    l_s = '둘리'
    a = 2
    print(locals())

print('===== Gloval Symbol Table VS Local Symbol Table =====')
print(globals())
g_f()

print(g_a)
#error : loca_symbol table은 함수가 실행이 끝나면 사라진다.
# print(l_a)
print("===== Object's Symbol Table =====")
# 1. 사용자 정의 함수
g_f.n = 'hello'
g_f.i = 10
print(g_f.__dict__)

# 2. 사용자 정의 클래스
class Myclass:
    def __init__(self):
        self.i = 10
        self.j = 20

    x = 10
    y = 10


Myclass.z = 10
print(Myclass.__dict__)


# 3. 내장함수
# 심벌테이블 X -> 확장을 할수 없다.
# print.z = 10
# print(print.__dict__)

# 4. 내장 클래스
# 심벌테이블 o -> 확장을 할수 있다.
# str.z = 10
print(str.__dict__)

# 5. 내장 클래스로 생성된 객체
# 심벌테이블 X -> 확장을 할수 없다.
# g_a. z = 10
# print(g_a.__dict__)

# 6. 사용자 정의 클래스로 생성된 객체
# 심벌테이블 o -> 확장을 할수 있다.
o = Myclass()
o.k = 30
print(o.__dict__)