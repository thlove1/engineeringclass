#==== list(append, insert, pop) ====

family = ["아빠", "엄마", "큰아들", "작은아들"]
print(family) # ['아빠', '엄마', '큰아들', '작은아들']

family.append("딸?") #append는 맨 뒤에 자료를 넣음
print(family) # ['아빠', '엄마', '큰아들', '작은아들', '딸?']

family.insert(4, "조카") #insert(위치, 데이터)
print(family) # ['아빠', '엄마', '큰아들', '작은아들', '조카', '딸?']

family.pop() # pop 뒤에서 하나씩 꺼냄
print(family) # ['아빠', '엄마', '큰아들', '작은아들', '조카']

family.pop()
print(family)  # ['아빠', '엄마', '큰아들', '작은아들']


#==== list(count, index, sort, reverse, clear) ====
family = ["아빠", "엄마", "아들", "아들", "딸"]
print(family.count("아들")) # 2
print(family.index("딸")) # 4

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]
# print(num_list.sort()) 작동안함.

num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]
# print(num_list.reverse()) 작동안함.

num_list.clear() # 리스트 내 자료 지우기
print(num_list) # []


#==== list(split, type, extend) ====
food = '삼겹살,라면,돈까스,피자'
food = food.split(',') #.split 하면 list로 변환 ['삼겹살', '라면', '돈까스', '피자']
print('내가 좋아하는 음식 : ', food)
print('type(food) : ', type(food)) # type(food) :  <class 'list'>

sid_list = ['100', 101, food] # 리스트 안에 문자, 숫자, 리스트 포함 가능.
print("sid_list: ", sid_list)
print("type(sid_list): ", type(sid_list))
print("sid_list[0]:", sid_list[0])                # 100 
print('type(sid_list[0]):', type(sid_list[0]))    # type(sid_list[0]): <class 'str'>

print("sid_list[1]:", sid_list[1])                # 101
print('type(sid_list[1]):', type(sid_list[1]))    # type(sid_list[1]): <class 'int'>

print("sid_list[2]:", sid_list[2])                # ['삼겹살', '라면', '돈까스', '피자']
print('type(sid_list[2]):', type(sid_list[2]))    # type(sid_list[2]): <class 'list'>

food.extend(sid_list) # extend 리스트 확장(결합)
print(food) # ['삼겹살', '라면', '돈까스', '피자', '100', 101, [...]]