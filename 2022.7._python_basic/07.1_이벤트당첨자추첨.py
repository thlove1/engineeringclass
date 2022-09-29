# 문제) 이벤트 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 준다.

# 조건 1: 20명 참여, 아이디를 1~20이라고 가정
# 조건 2: 무작위 추첨하되 중복 불가
# 조건 3: random 모듈의 shuffle과 sample 활용

# 출력예시
# --- 당첨자 ---
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다.--

from random import *
lst = [1,2,3,4,5]
print(lst)   # [1, 2, 3, 4, 5]
print(sample(lst,1)) # [1] / [4] 등 sample(lst에서, 1개를 무작위로 추출)

shuffle(lst) # lst 안의 값을 무작위로 바꿈
print(lst)   # [4, 3, 2, 5, 1]
print(sample(lst,1)) # [5] / sample(lst에서, 1개를 무작위로 추출)

users = range(1, 21) # 1부터 20까지 숫자를 생성
print(type(users)) # <class 'range'>
users = list(users) # random 패키지의 shuffle 함수를 사용하기 위해 list로 type 변경
print(type(users)) # <class 'list'>

print(users)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(users)
print(users)  # [7, 2, 5, 19, 15, 11, 18, 16, 3, 13, 9, 1, 17, 14, 10, 8, 12, 6, 4, 20]

rule2 = sample(users, 4) # 1명 뽑고 나머지 3명 뽑으면 중복 될 수 있어 한번에 4명 뽑는다.

print("--- 당첨자 ---")
print("치킨 당첨자 : {}".format(rule2[0]))
print("커피 당첨자 : {}".format(rule2[1:]))
print("-- 축하합니다.--")

print("--- 당첨자 ---")
print("치킨 당첨자 : ", rule2[0])
print("커피 당첨자 : ", rule2[1:])
print("-- 축하합니다.--")