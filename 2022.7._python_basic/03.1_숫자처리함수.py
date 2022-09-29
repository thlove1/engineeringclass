# ==== 숫자처리함수(abs, pow, max, min, round, bin, floor, ceil, sqrt) ====

print(abs(-5)) #5 / abs( ) 절대값
print(pow(4, 2)) #16 / pow(a, b) a^b

print(max(5, 12))
print(min(5, 12))

print(round(3.14)) # 3 / 반올림
print(round(3.14,1)) # 3.1 / 소수 첫번째 자리까지 표현 반올림
print(round(4.94)) # 5 / 반올림
print(round(4.94,1)) # 4.9 / 소수 첫번째 자리까지 표현 반올림

print(bin(2)) # 0b10 / bin(숫자)를 2진수로 변환
print(bin(3)) # 0b11
print(bin(4)) # 0b100
print(bin(5)) # 0b101 

from math import * # math 라이브러리 안에 있는 모든 것을 이용하겠다.
print(floor(4.94)) # 4 / 내림 
print(ceil(3.14)) # 4 / 올림
print(sqrt(16)) # 4.0 / 제곱근(무엇의 제곱이니?)