# # 변수 선언 방법
# # 변수 이름 = 값
# # 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
# temp = 36 # 숫자로 저장하고 싶다면 따옴표 금지
# name = "센서 A" # 글자는 무조건 따옴표로 감싸기

# print(temp) #36
# print("temp") #temp

# # = 은 "같다"가 아니라 "저장"하는 것
# # 비교는 ==을 사용

# #======================
# print("=====변수 사용 활용=====")

# x=5
# #변수에 할당할때 오른쪽을 먼저 계산한뒤 x에 값을 재할당
# #변수를 "재활당"할 때 변수 기존 자신의 값을 활용할 수 있음
# x=x+5 
# print(x) #10
# #y=y+5 #오류발생 y가 선언되지 않았기 때문

# #=======================
# print("==========재할당=======")
# print("재할당하기전 temp:", temp)
# temp = 15 #위에서 할당했던 36이라는 값을 15로 재할당(수정)
# Temp = 150 #temp와 다른 변수로 동작
# print("temp:", temp,)
# print("Temp:", Temp)
# #재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴
# #print(score) # Name Error 발생
# score = 10 
# print(score) # 10
# score = 20 
# score = 30
# print(score) #30

# #=======================
# print("========값 복사 =======")

# a = 10
# b = a #b 변수에는 10이 저장(저장할때의 그 순간의 a값을 b에 복사)
# a = 100 #a변수를 재할당해도 
# print(b) # 10 b변수의 값은 10이 그대로 유지됨

# #=======================
# print("========여러 변수 한번에 선언 및 할당 =======")
# # 형식: 변수1, 변수2,... = 값1, 값2,... <변수와 값의 갯수가 같아야 함
# width, height = 10,20 # width 는 10 height 는 20
# print("width:", width)
# print("height:", height)

# #x,y,z+10,20 #변수 3개, 값 2개 > value Error 발생

# #=======================
# print("========주석으로 변수 설명 =======")
# temp = 25 # 온도 (섭씨)
# count = 3 # 센서 개수
# #temp = 100000000 # 주석 처리된 코드는 동작하지 않음 
# print(temp) # 20


# temp = 25
# print(temp)
# name = "센서 A"
# print(name)

# temp = 30
# print(temp)
# temperature = 25
# print(temperature)

my_number=5
print(my_number)
mood="기쁨"
print(mood)

age=24
label = "나이"
print(label)
print(age)

x = 10
print(x)
x = x+5
print(x)
x = x*2
print(x)

a = 100
b = a
a = 999
print(a)
print(b)

temp = 25
print(temp)
score = 90
#print(Score)
print(score)

temp = 25 # 온도(섭씨)
count = 3 #센서 개수
#temp = 100 # 실행 되지 않음
print(temp) #25 출력

x = 5
x = 10
x = x+1 
print(x)

name = "센서 A"
temp = 25
print("설비")
print(name)
print(temp)

a = 24
device_temp = 24
print(device_temp)

x,y,z = 1,2,3
width, height= 4,3
print(width)
print(height)
