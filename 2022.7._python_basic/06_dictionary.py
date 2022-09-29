#==== dictionary(keys, values, items, in, dic[key], dic.get(key)) ====
#dictionary는 { } 로 표시 {key : value}  / key와 value는 문자, 숫자 모두 가능

dic = { 2 : "김진연", 1 : "양OO", 3 : "큰아들", 4 : "작은아들"}
print("key 목록:", dic.keys())              # key 목록: dict_keys([2, 1, 3, 4])  
print("value 목록:", dic.values())          # value 목록: dict_values(['김진연', '양OO', '큰아들', '작은아들'])
print(dic.items())                          # dict_items([(2, '김진연'), (1, '양OO'), (3, '큰아들'), (4, '작은아들')])
print(dic)                                             # {2: '김진연', 1: '양OO', 3: '큰아들', 4: '작은아들'}
print("type :", type(dic))                  # type : <class 'dict'>
print(2 in dic) # True
print(7 in dic) # False
print("김진연" in dic) # False (in)은 키 값만 있는지 없는지 확인 가능

print(dic[1]) # 양OO
print(dic.get(1)) # 양OO
print(dic[5]) # KeyError: 5 에러를 표기하고 이후 종료되어 dic.get(5)로 사용해야(None) 이후 실행된다는 내용도 있으나 실행됨.
print("딸?")
print(dic.get(5,"딸!")) # key 값 5를 찾고 없을 경우 "딸!"을 표기
print(dic.get(5)) # None / "딸!"이 포함되는 것은 아님.


#==== dictionary(추가, 수정, 일부삭제(del), 모두삭제(clear)) ====
dic[5] = "딸"  # 새로운 key와 vlue를 넣는법
dic[6] = 0     # value에 숫자도 가능
dic["넷째는"] = "없다"     # key에 문자도 가능
print(dic)     # {2: '김진연', 1: '양OO', 3: '큰아들', 4: '작은아들', 5: '딸', 6: 0, '넷째는': '없다'}

dic[6] = "없다"     # key(6)에 해당하는 값을 바꿀 수 있다.
print(dic)     # {2: '김진연', 1: '양OO', 3: '큰아들', 4: '작은아들', 5: '딸', 6: '없다', '넷째는': '없다'}

del dic[6] # del dic[6, "넷째는"] 한번에 여러 키를 지우는 건 않된다.
print(dic)     # {2: '김진연', 1: '양OO', 3: '큰아들', 4: '작은아들', 5: '딸', '넷째는': '없다'}
del dic["넷째는"]
print(dic)     # {2: '김진연', 1: '양OO', 3: '큰아들', 4: '작은아들', 5: '딸'}

dic.clear()   # 모든 key와 value 삭제
print(dic)    # {}


#==== dictionary(key-문자, value-문자) ====

mydata = {"이름" : "김진연", "직업" : "기술교사", "별자리" : "물고기자리"}  
print("mydata :", mydata)                           # mydata : {'이름': '김진연', '직업': '기술교사', '별자리': '물고기자리'}
print("mydata['이름'] :", mydata['이름'])            # mydata['이름'] : 김진연
print("mydata.get('이름') :", mydata.get('이름'))    # mydata.get('이름') : 김진연



#==== dictionary(활용 - dic 안에 dic) ====

myfamily = {"아빠" : {"이름" : "김진연", "별자리" : "물고기자리"},
            "엄마" : {"이름" : "양OO", "별자리" : "양자리"},  
            "큰아들" : {"이름" : "김범수", "별자리" : "사자자리"},  
            "작은아들" : {"이름" : "김민수", "별자리" : "황소자리"} }

print("myfamily :", myfamily)                                                # myfamily : {'아빠': {'이름': '김진연', '별자리': '물고기자리'}, 
                                                                             #               '엄마': {'이름': '양OO', '별자리': '양자리'}, 
                                                                             #               '큰아들': {'이름': '김범수', '별자리': '사자자리'}, 
                                                                             #               '작은아들': {'이름': '김민수', '별자리': '황소자리'}}
print("mydata['아빠'] :", myfamily['아빠'])                                   # mydata['아빠'] : {'이름': '김진연', '별자리': '물고기자리'}
print("mydata['아빠']['별자리'] :", myfamily['아빠']['별자리'])                    # mydata['아빠']['별자리'] : 물고기자리
print("mydata.get('아빠').get('별자리') :", myfamily.get('아빠').get('별자리'))    # mydata.get('아빠').get('별자리') : 물고기자리