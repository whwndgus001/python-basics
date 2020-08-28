# enumerate() 함수 사용하기

index = 0
for color in ['red', 'yellow', 'blue', 'black', 'gray']:
    print(index, color)
    index = index + 1

for index, in enumerate ['red', 'yellow', 'blue', 'black', 'gray']:
    print(index, color)