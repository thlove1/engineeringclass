# ==== 산술연산자(*, /, //, %) ====
print(5 * 2)
print(10 / 4)
print(10 // 3) #10을 3으로 나눈 몫
print(10 % 3) # 10을 3으로 나눈 나머지 값

a = 1 + 2 + 3 # 6
a = a + 4 #10
a += 5 #15, A *= 5 => A = A * 5
print(a)

# ==== 비교연산자(==, !=, >=) ====
num = 3 # 오른쪽에 있는 3(값)을 변수 num에 대입
num == 3 # num과 3이 같다면 true. 다르다면 false
num != 3 # num과 3이 같지 않다면 true, 같다면 false
num >= 3 # num이 3보다 크거나 같으면 true, 아니면 false
num > 3 # num이 3보다 크면 true, 아니면 false


# ==== is 연산자 / is not 연산자(불 연산자) ====
# A is B : A와 B가 동일 주소에 할당된 객체인지 비교, 동일 주소이면 true
# 
a = 1
b = 1.0
print(a == b) # true
print(a is b) # false
print(id(a))  # 1944521933040
print(id(b))  # 1944522971824

print(ord('a')) # 97 문자'a'의 아스키코드 값


# ==== in 연산자 / not in 연산자 ====
# 'A' in 'B'  'A'문자열이 'B'문자열에 포함되어 있으면 true
'a' in 'banana' # 'a'가 'banana'에 포함되어 있음으로 true
'seed' in 'banana' # flase

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
            
in_both('apples', 'oranges') 
# a
# e
# s

# ==== 논리 연산자(and, or, not) ====
print(not True and False or not False) # True / 논리 연산자가 식 하나에 들어 있으면 not -> and -> or 순으로 판단

# ==== 비트 연산자(&, |, ^, ~) ====
# &(and), |(or, shift backslash), ^(XOR: 같으면 false, 다르면 true), ~(not)
print(bin(13)) # 0b1101 : bin(정수) 10진수를 2진수로 된 문자열로 변환
print(0b1101) # 13 : 2진수는 10진수로 즉시 변환

print(bin(9)) # 0b1001
print(0b1001) # 9
print(bin(0b1101 ^ 0b1001)) # 0b100 

print(13 ^ 9) # 4
print(bin(4)) # 0b100 
