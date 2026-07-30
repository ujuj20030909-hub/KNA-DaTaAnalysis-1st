# 실습
# n = int(input("끝 숫자 N: "))
# for i in range(1, n + 1):
#     print(i)
# for i in range(2, n + 1, 2):
#     print(i)
# for i in range(n, 0, -1):
#     print(i)

# 3의 배수 출력하기
# 사용자에게 범위를 입력받아 3의 배수 출력하기
# 예)
# 사용자 입력값: 20
# 출력값: 3, 6, 9, 12, 15, 18
# for문 , if문, 나머지 연산자
# 4 % 3 == 0
# print(3 % 3) # 0
# print(4 % 3) # 1
# print(5 % 3) # 2
# print(6 % 3) # 0

# n = int(input("범위: "))
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         print(i)

# 1~9단 사이 2의 배수 단만 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        if i % 2 == 0:
            print(f"{i} X {j} = {i * j}")
print(f"=== {i}단 끝 ===")
