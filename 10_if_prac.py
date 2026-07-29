# if문 실습
# 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성하기
# 성인이라면 "성인입니다", 미성년자라면 "미성년자입니다." 출력

# age = int(input("나이는:"))
# if age == 24:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# 숫자 맞추기 게임
# 정답은 임의로 지정
# 정답을 맞추면 맞았습니다, 틀리면 틀렸습니다 출력

# 예시
# 정답을 50으로 지정
# 사용자에게 입력값 받기
# 사용자 입력값이 정답과 동일하다면 "정답입니다" 출력
# 사용자 입력값이 틀렸다면 "틀렸습니다" 출력
# 마지막으로 무조건 "게임이 종료되었습니다" 출력

# result = 45
# score = int(input("정답은?:"))
# if score == 45:
#     print("정답이에요!😎")
# else:
#     print("재도전하세요.😢")
# print("게임이 종료되었습니다.🤡")

# 신호등 색을 입력받아서
# "초록색" 이라면 "건너세요" 출력
# "빨간색" 이라면 "기다리세요" 출력
# 입력값이 초록색이나 빨간색이어야만 정상 동작하는 점 유의
# 이상한 값 입력 시 "다시 입력하세요" 출력

# user = input("색을 입력하세요 (빨간색, 초록색만 입력 가능):")

# # or 사용 + if문 중첩
# if user == "초록색" or user == "빨간색":
#     # user이 "초록색"이거나 "빨간색"일 때만 실행
#     if user == "초록색":
#       print("건너세요!") # 중첩 if문은 들여쓰기 더 주의
#     # if user == "빨간색": # else문과 동일하게 동작
#     #  print("기다리세요!") # 하지만 else 를 사용하는게 효율적
#     else:
#       print("기다리세요")
# else:
#   print("다시 입력하세요")

# and 연산자 + 중첩

# 사람 체온 판단
# 정상 체온 범위: 36.2~36.9

# user_a = float(input("체온을 입력해주세요: "))

# if user_a >= 36.2 and user_a <= 36.9:
#    print("당신은 정상 체온입니다.")
# else:
#     if user_a > 36.9:
#       print("당신은 열이 나고 있습니다.")
#     else:
#       print("당신은 저체온 입니다.")
# print("체온 판단 완료")

# 위의 체온 판단 if문 안에서 열나는지 저체온인지 판단하도록 수정

# user_a = float(input("체온을 입력해주세요: "))

# if user_a >= 36.9 or user_a <= 36.2:
#     # if문 중첩 자체는 무한히 가능
#     # 권장하지는 않음
#     if user_a > 36.9:
#         print("당신은 열이 나고 있습니다.")
#     else:
#         print("당신은 저체온 입니다.")
# else:
#     print("당신은 정상 체온입니다.")

# print("체온 판단 완료")


# if user == "초록색":
#     print("건너세요!")

# if user == "빨간색":
#     print("기다리세요!")
# else:
#     print("다시 입력하세요!")

# elif
# else와 if만으로 분기하기에는 불편하고
# if 중첩이 너무 많아져서 생김
# if user <= 36.2:
#     print("당신은 저체온입니다.")
# elif user >= 36.9 and user < 37.8:
#     print("당신은 미열입니다. 주의하세요.")
# elif user >= 37.8:
#     print("당신은 고온입니다. 병원에 가세요.")
# else:
#     print("당신은 정상체온입니다.")
# print("체온 확인 완료")

# temp = int(input("온도: "))
# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")

# id = "ujuj"
# pw = "0909"
# user_id = input("아이디: ")
# user_pw = input("비번: ")
# if id == user_id and pw == user_pw:
#     print("로그인 성공")
# else:
#     print("로그인 실패")

temp = int(input("온도: "))
vib = float(input("진동: "))
cur = int(input("전류: "))

if temp > 80 or vib > 4.0:
    print("위험: 즉시 정지")
else:
    if cur > 60 and temp > 70:
        print("주의: 부하 점검")
    elif vib > 2.5:
        print("주의: 진동 관찰")
    else:
        print("정상")
