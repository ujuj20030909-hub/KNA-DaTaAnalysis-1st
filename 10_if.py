# 조건문 - if
# 항상 실행되지 않고 조건에 따라서
# 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True와 False로 결과가 나와야 함

# if 조건식:
#   실행할 코드 (한 칸 들여쓰기 tab)

# if문의 :은 그 다음 올 코드가
# if문 조건식 결과가 True일 때만 실행하라는 의미
# 즉, 여기서부터 이 조건에 속한다라는 신호
# 조건에 속하는 코드는 모두 들여쓰기가 적용되어있어야 함
# 들여쓰기 한 코드는 if문의 조건식 결과가 True일 때 실행

temp = 85

if temp > 80:  # 만약에 temp라는 변수에 담긴 값이 80보다 크다면?
    print(" temp 변수의 값이 80보다 크다!!!!")  # 들여쓰기 된 코드 실행
    print(" 🚨 ")
print("이건 항상 실행되는 코드")

temp = 50
if temp > 80:
    print(" temp 변수의 값이 80보다 크다!!!!")
    print(" 🚨 ")
print("이건 항상 실행되는 코드")

# temp 변수의 값이 80보다 크다면 "경고" 출력
# temp 변수의 값이 80보다 이하라면 "정상" 출력
# 위 두 가지를 모두 하고싶은 경우

temp = 70  # 1, 2안 모두 정상 출력
temp = 90

# 1안
if temp > 80:
    print("경고")
print("정상")  # if문 밖의 코드는 무조건 실행됨
# 이 경우에는 temp 변수의 값이 90이어도 실행되는 것

# 2안 > else 사용
if temp > 80:
    print("경고")
else:  # if문의 조건이 False일 때만 출력
    print("정상")  # 항상 실행되지 않음
# if문의 코드블럭과 else문의 코드블럭은 절대 동시에 실행되지 않음
# 둘 중의 하나만 실행
# 2개의 분기로 코드를 실행해야할 때 사용

# elif
# else와 if만으로 분기하기에는 불편하고
# if 중첩이 너무 많아져서 생김
if user <= 36.2:
    print("당신은 저체온입니다.")
elif user >= 36.9 and user < 37.8:
    print("당신은 미열입니다. 주의하세요.")
elif user >= 37.8:
    print("당신은 고온입니다. 병원에 가세요.") 
else:
    print("당신은 정상체온입니다.")
print("체온 확인 완료")  

# elif의 순서

score = 50

if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
elif score >= 50:
    print("미흡")
else:
    print("비상")

# elif 순서 주의

score = 100

if score >= 50: 
    print("미흡")
elif score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
else:
    print("비상")
# 50이 먼저 있어서 미흡이 나옴

# not 연산자
# 괄호로 감싸서 사용
if not (3 == 5):
    print("출력됩니다")
# 3과 5는 같지 않으니 False가 되지만
# 앞에 not이 있어서 False를 True로 뒤집어 if가 인식

# if문은 줄바꿈을 하지않아도 :을 기준으로 동작 자체는 가능
# 하지만 줄바꿈해서 가독성을 높이길 권장
# 탭은 아직 위의 코드가 끝나지 않았고 한줄이라는 것을 명시
