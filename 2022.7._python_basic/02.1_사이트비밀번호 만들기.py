# 문제) 사이별로 비밀번호를 만들어 주는 프로그램을 작성하오.

# 예) https://naver.com

# 규칙1 : https:// 부분은 삭제 => naver.com

# 규칙2: 처음 만나는 점(.) 이후 부분을 삭제 => naver

# 규칙3: 비밀번호는 남은 글자 중 처음 세자리(nav) + 글자 갯수(5, naver) + 글자내 'e'의 갯수(1) + "!"
# 예) 생성된 비밀번호: nav51!

site = "https://naver.com"

rule1 = site.find("/")
print(rule1)
print(site[rule1+2:])

rule1 = site[rule1+2:]
# 또는 rule1 = site.replace("https://","") 하지만 이 방법은 http://는 적용안됨.

rule2 = rule1[:rule1.find(".")]
print(rule2)

rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
print(rule3)

print("{}의 비밀번호는 {}입니다.".format(site, rule3))