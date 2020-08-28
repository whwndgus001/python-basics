# 문제 1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요.

try:
    a = int(input('수를 입력하세요:'))
    if a%3 ==0:
        print('3의 배수')
    elif a%3 !=0:
        print('3의 배수가 아닌 수')
    else:
except ValueError as e:
    print('정수가 아닙니다')

# import sys
#
# number = input ('수를 입력하세요:')
#
# print(number , type(number))
# number = int(number)
# if number > 10:
#     sys.exit()
#
# print("ok")


