# for 반복문
# for   in  [sequnce 객체] :
for number in [10, 20, 30, 40] :
    result = number**2
    print (result, '----', end=' ')
else:
    print('')


a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')

# 복합 자료형을 for문에서 사용하는 경우
l = [('둘리', 10), ('마이콜', 30),('또치', 11)]
for t in l:
    print('이름: %s, 나이:%d' %t)

# 10번 반복하는 Loop
for i in range(1, 11):
    print(i, end=' ')
else:
    print('\n---------------------')

# 1 ~ 10 합을 구하기
sum = 0
for i in range(1, 11):
    sum=sum+i
print(sum)

# break
for n in range(10):
    if n > 5 :
        break
    print(n, end=' ')
else:
    print('\n-------------')

print("\n-------------------")
# continue
for n in range(10):
    if n <= 5 :
        continue
    print(n, end=' ')
else:
    print('\n-------구구단 1-----')

for i in range(1, 10):
    for j in range (1, 10):
        print("%d x %d = %d" % (i, j, i*j))

    print("\n-----------구구단 2----------")

#구구단
for i in range(1, 10):
    for j in range(1, 10):
        print("{0} x {1} = {2}" .format (j, i, j * i), end='\t')
    else:
        print('')

print('\n-----------삼각형-----------')
for i in range(10):
    for j in range(0 ,i+1):
        print('*', end='')
    else:
        print('')

print('\n--------삼각형2-------------')
for i in range(10, 0, -1):
    print('*' * i)