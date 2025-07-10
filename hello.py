'''
# 자료의 형태 
# 변수 : 그릇, 상자
a = 100 # 숫자 -> 정수 -> integer -> int
b = "강아지" # 문자열 -> string -> str

# 숫자
# 정수, 실수
# 실수 : 3.14, -3.14, 5.555 -> float
# type(a) 어떤 타입인지 알려주는 함수

# 문자열
a = "abcde" 
a[0:3] # 0번째부터 3번째 전까지 수 -> abc
A = "aaaabbbccd"
A.count("a") # A라는 변수에 a가 몇 개인지
# len() 변수의 길이를 알려주는 함수

# bool -> True False (하나의 자료 형태) ex.조건문
3 == 3 # ==는 두 개가 같는지 묻는 기호

# list
a = ["강아지", "고양이"] # 1차원 배열
b = [[1,2,1,3],
     [1,0,0,2]] # 2차원 배열 (유저의 개인정보, 게임에서의 위치)
a = [1, 2, 3, True, 1.14, "강아지", [1, 2, 3, 4]]
a.append("사람") # list 마지막에 사람이라는 값이 추가
a.remove("고양이") # list 안에 고양이를 제거 (고양이가 list에 두 개가 있다면 맨 앞의 값이 제거)
del a[1] # 인덱스 번호로 제거
a[0] = "개" # a의 0번째를 개로 수정
a[0][0] #  a라는 값에 0번째에 있는 값에 0번쨰를 가져옴 

# tuple
a = tuple(1, 2, 3, 4, 5) # list랑 똑같은데 오직 읽기만 가능 제거, 수정 등 불가
a.count, index만 있음

# set
a = set((1, 2, 3, 4, 5)) # 순서가 없고 중복 x -> 중복을 제거할 때 자주 사용
a = "jenjfnefijdosjwlijawldifnqo"
print(list(set(a)))

# http 는 서버간 약속, https 는 s 는 보안
# JSON 은 데이터를 교환하고 저장할 때 정해진 구조
# dict
a = dict() # key와 value로 이루어짐, ket는 중복 x
a["이름"] = "홍길동"
a["나이"] = 50
a["직업"] = "백수"
print(a)
# print(a.keys()), print(a.values()) 

# 조건문 

# 횟수 제어 반복, 조건 제어 반복

# 연산자, 약속된 기호, 산술 연산자, + - * / // %
# 대입 연산자, a = 100 왼쪽의 값에 오른쪽 값을 대입한다

# 비교 연산자, 6가지 
# ==(같니?), !=(다르니?), >, <, >=, <=
print(3 == 3) or print(3 != 3) #True or False

score = int(input("시험 점수를 입력하세요 : "))
if 90 <= score <= 100 :
    print("당신은 1등급 입니다.")
elif 80 <= score <= 89 :
    print("당신은 2등급 입니다.")
else :
    print("당신은 3등급 입니다.")

#숫자 하나를 입력받고 그 수가 짝수인지 홀수인지 구별
num = int(input("숫자를 입력하세요 : "))
if num % 2 == 0 :
    print(num, "은 짝수입니다.")
else :
    print(num, "은 홀수입니다.")

name = input("이름 : ")
age = int(input("나이 : "))
if len(name) == 3 :
    if name[0] == "김" :
        if age >= 10 :
            print("가입 완료")
    elif name[0] == "이" :
        if age >= 10 :
            print("가입 완료")
    elif name[0] == "박" :
        if age >= 10 :
            print("가입 완료")
else :
    print("가입 불가")

# 논리 연산자, and, or

# and 는 내용이 True만 있어야 True 
# or 은 내용이 True 하나만 있어도 True

name = input("이름 : ")
age = int(input("나이 : "))
if len(name) == 3 : and (name[0] == "김" or name[0] == "이" or name[0] == "박") and age >= 10 :
'''

# min, max
# a = [1,2,3,4,5,6,7,8]
# print(max(a)) -> 리스트 안에 가장 큰 값 출력 

# inprot random  -> 내장 라이브러리, 외장 라이브러리 -> django, numpy 등

'''
import random
d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
print(d1, d2, d3)

if d1 == d2 == d3 :
    score = d1 * 10000
elif d1 == d2 or d2 == d3 :
    score = d2 * 1000
elif d1 == d3 :
    score = d1 * 1000
else :
    score = max(d1, d2, d3) * 100
print("당신의 점수는 : ",score)

# F = F + 1 -> F += 1
# 몬테카를로
import random

f = 0
b = 0
count = 100
for i in range(count) :
    coin = random.randint(1,2)
    if coin == 1 :
        f += 1
    elif coin == 2 :
        b += 1
print(f)
''' 
