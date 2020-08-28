# 1 ~ 10 합을 구하기
s = 0
# for n in range(1, 11):
#   s +=n
# print(s)


s, count = 0, 1
while count < 11:
    s += count
    count +=1
print(s)

# break

# for n in range(10):
#     if n > 5 :
#         break
#     print(n, end=' ')
# else:
#     print('\n-------------')

i = 0
while i < 10:
    if i > 5:
        break
    print(i, end= ' ')
    i += 1
print('\n-------------------------------------')

# for n in range(10):
#     if n <= 5 :
#         continue
#     print(n, end=' ')
# else:
#     print('\n-------구구단 1-----')
i = 0
while i < 10:
    if i <= 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1

print('\n---------------------------------------')

# 무한루프
i = 0
while True:
    print(i, end = ' ')
    if i > 5:
        break
    print('infinite roop')