def dummy():
    pass

def my_function():
    print('Hello World')


def my_function2():
    return 10, 20


def my_function3(id):
    print('{0}님 안녕하세요'.format(id))



def my_function4(a, b):
    return a * b


def none():
    print('some codes...1')
    if 10 - 9 is 1:
        return
    print('some codes...2')

# 함수는 객체다. (함수를 값 처럼 다룰 수 있다.)
def my_function5():
    f()

dummy()
my_function()

#t = my_function2()
i, j = my_function2()
print(i, j)

my_function3('96J_J')

r = my_function4(10, 20)
print(r)

# my_function5(my_function)
print((my_function), type(my_function))