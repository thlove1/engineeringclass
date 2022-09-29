#==== tuple ====
# 내용 변경이나 추가를 할 수 없음. 단 속도가 리스트보다 빠름. 변경되지 않는 목록에 사용.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김진연"
major = "기술교육"
job = "기술교사"
print(name, major, job) # 김진연 기술교육 기술교사

(name, major, job) = ("김진연", "기술교육", "기술교사")
print(name, major, job) # 김진연 기술교육 기술교사