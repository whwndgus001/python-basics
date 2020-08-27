# 문제 3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
# * 1부터 10개 까지 출력
a=10
for i in range(a):
    for j in range(a+1):
        if j <= i :
            print("*" , end = "")
    print()

# a = 10
# for i in range(a):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(a+1):    # 0부터 4까지 5번 반복. 가로 방향
#         if j <= i:                # 세로 방향 변수 i만큼
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
#                # (print는 출력 후 기본적으로 다음 줄로 넘어감)