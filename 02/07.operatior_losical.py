# 일반적으로 피연산자(operand)는 True 또는 False 값을 가지는 연산
# not True = False
# not False = True
a = 20
print (not a < 20)



# True and True = True
# True and False = False
# False and True = False
# False and False = False
print (a < 30 and a != 30)

# True or True = True
# True or False = True
# False or True = True
# False or False = False
print(a == 30 or a > 30)

# 논리식의 계산순서
print(True or bool('logical'))
print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([] and 'logical')
print([2,10] and 'logical')




def f():
    print('hello world')


a = 20
#if a > 10:
#    f()
a > 10 or f()

s = 'hello world'
s and print(s)