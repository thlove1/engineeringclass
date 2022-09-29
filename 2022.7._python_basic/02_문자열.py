print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# ==== len(), \', \", \\ ====

sentence = '나는 김진연 입니다.'
print(sentence)
len(sentence) # 11 / ' ' 사이의 한글과 빈칸 . 을 포함한 갯수(리스트의 갯수도 알 수 있음)

sentence2 = "파이썬은 재미있어요"
print(sentence2)

sentence3 = """
나는 김진연이고,
파이썬은 쉬워요
"""
print(sentence3)

sentence4 = '나는 "김진연"이야' # 나는 "김진연"이야 / " "를 출력하기 위해서는 ' '로 묶어주면 됨
print(sentence4)

sentence5 = "나는 \"김진연\"이야" # 나는 "김진연"이야 / " "를 출력하기 위해서는 \"  "\로 묶어주면 됨
print(sentence5)

sentence6 = "나는 '김진연'이야." # 나는 '김진연'이야 / ' '를 출력하기 위해서는 "  "로 묶어주면 됨
print(sentence6)

sentence7 = '나는 \'김진연\'이야.' # 나는 '김진연'이야 / ' '를 출력하기 위해서는 \'  \'로 묶어주면 됨
print(sentence7)

sentence8 = "C:\Users\ahora\Desktop\2022.7._python_basic\02_문자열.py" # 오류 / 문장 내 \를 표기하기 위해서는 \\ 사용
print(sentence8)

sentence9 = "C:\\Users\\ahora\\Desktop\\2022.7._python_basic\\02_문자열.py" # C:\Users\ahora\Desktop\2022.7._python_basic\02_문자열.py
print(sentence9)

# ==== 탈출문자(\n, \r, \b, \t) ====

print("백문이 불여일견\n백견이 불여일타") # \n 은 줄바꿈
#백문이 불여일견
#백견이 불여일타

print("Red Apple \rPine") # PineApple / \r은 커서를 맨 앞으로 보냄
print("RedApple \rPine") # Pinepple / 'A'가 없어짐. 새로 쓰는 문자의 수 고려 필요
print("RedApple \r Pine") #  Pineple / 'Ap'가 없어짐. \r뒤에 공백도 인식함

print("Redd\bApple") # RedApple / \b 앞글자를 지우고 뒤 문자를 이어서 작성함

print("Red\tApple") # Red     Apple / \t는 Tab 기능


# ==== 슬라이싱 ====
jumin = "050302-3456789"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0~2 직전까지 / 가져올 자리 1보다 하나 더 큰수 적어야 함
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6]) # jumin[:6] 과 동일
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 : " + jumin[-7:]) # 뒤에서 부터 계산(맨 뒷자리 수 9는 -1번째 자리임)


# ==== 문자열처리 함수(lower, upper, isupper, replace) ====
text = "Python is Amazing"
print(text.lower()) # 소문자로 출력 / python is amazing
print(text.upper()) # 대문자로 출력 / PYTHON IS AMAZING
print(text[0].isupper()) # text[0] 가 대문자인지 확인 true or false / True
print(text.replace("Python", "Java")) # 원하는 문장을 찾아서 바꿔줌 / Java is Amazing
print(text) # Python is Amazing 


# ==== 문자열처리 함수(index, find, count) ====
index = text.index("n") # n이 몇번째 글자인지 알려줌
print(index) # 5

index = text.index("n", index + 1) # 2번째 나오는 n이 몇번째 글자인지 알려줌 / index의 두번째 파라미터는 검색 출발점
print(index) # 15

print(text.find("n"))  # 5 / find는 찾는 값이 없을 경우 -1을 출력, index는 오류값이 나오며 프로그램 종료.

print(text.count("n")) # 2 / 2개가 있다.


# ==== 문자열포멧(%s) ====
print("a" + "b") # ab
print("a", "b") # a b

print("나는 %d살 입니다." % 18) # 나는 18살 입니다. / d에는 정수만 들어갈 수 있음 
print("나는 %s을 좋아해요" % "파이썬") # 나는 파이썬을 좋아해요 / s는 문자열
print("Apple은 %c로 시작해요." % "A") # Apple은 A로 시작해요. / c는 문자 한개

mun = "감자"
print(mun + "는 %c으로 시작해요." % mun[0]) # 감자는 감으로 시작해요.

print("나는 %s살 입니다." % 18) # 나는 18살 입니다. / %s를 사용하면 모두(소수도) 입력 가능

print("나는 %s색과 %s색을 좋아해요." %("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요.

# ==== 문자열포멧({}와 .format()), f ====
print("나는 {}살 입니다.".format(18)) # 나는 18살 입니다. / format()에 있는 데이터를 {}에 넣음
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요.".format("파랑", "빨강")) # 나는 파랑색과 빨강색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강")) # 나는 빨강색과 파랑색을 좋아해요.


print("나는 {age}살이며, {color}색을 좋아해요.".format(age=18, color="빨강")) # 나는 18살이며, 빨강색을 좋아해요.

age = 18
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # 나는 18살이며, 빨강색을 좋아해요.