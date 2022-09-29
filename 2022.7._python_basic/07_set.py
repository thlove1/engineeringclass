#==== set(set([]), (교집합)intersection, (합집합)union, (차집합)difference, (추가)add, (삭제)remove) ====
#중복이 되지 않고, 순서가 없다.

my_set = {4, 1, 2, 3, 3, 3}
print(type(my_set)) # <class 'set'> / dictionary는 { key : value } 형태
print(my_set) # {1, 2, 3, 4}

lanc = {"김진연", "양OO", "김범수"}
python = set(["김진연", "김민수"])

#교집합 - C언어와 Python 모두 할 줄 아는 사람
print(lanc & python) # {'김진연'}
print(lanc.intersection(python)) # {'김진연'}

#합집합  - C언어 또는 Python 할 줄 아는 사람
print(lanc | python) # {'김범수', '김민수', '양OO', '김진연'}
print(lanc.union(python)) # {'김범수', '김민수', '양OO', '김진연'} / 순서는 달라질 수 있음.

#차집합  - C언어 할 줄 아는 사람 중 Python 못 하는 사람
print(lanc-python) # {'김범수', '양OO'}
print(lanc.difference(python)) # {'김범수', '양OO'}

# (추가) python 할 줄 아는 사람이 늘어남
python.add("김혜수")
print(python) # {'김민수', '김혜수', '김진연'}

# (제거) c언어를 잊었어요.
lanc.remove("김진연")
print(lanc) # {'김범수', '양OO'}


#==== 자료구조의 변경 ====

menu = {"커피", "우유", "주스"}

print(menu, type(menu)) # {'커피', '주스', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['커피', '주스', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('커피', '주스', '우유') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'set'>