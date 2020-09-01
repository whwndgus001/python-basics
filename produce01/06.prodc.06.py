# 문제6.
# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권,
# 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환
# 되는지 작성하시오.
# comprehension

a = int(input('정수를 입력하세요 : '))
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
money = []


count_50000 = money // 50000
count_10000 = money // 10000
count_5000 = money // 5000
count_1000 = money // 1000
count_500 = money // 500
count_100 = money // 100
count_50 = money // 50
count_10 = money // 10
count_1 = money // 1

print("50000권의 개수", count_50000)
print("10000권의 개수", count_10000)
print("5000원권의 개수", count_5000)
print("1000원권의 개수", count_1000)
print("500원권의 개수", count_500)
print("100원권의 개수", count_100)
print("50원권의 개수", count_50)
print("10원권의 개수", count_10)
print("1원권의 개수", count_1)