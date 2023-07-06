# key 와 value >> key 에 대한 중복은 허용되지 않음

cabinet = {3:"유재석" , 4 : 2 , 6 : "왕간다가간다" , 5: "호날두"}

print(cabinet[4])
print(cabinet[6])
print(cabinet.get(3))
print(cabinet.get(0)) # None 이라는 값이 return 된다  <--> [key] 로 접근하면 오류가 난다
print(cabinet.get(0,"사용가능"))
print(3 in cabinet) # true false 반환

# key 는 굳이 int가 아니여도 됨 index와 다른개념
print(cabinet)
cabinet[20] = "조세호" # 이렇게 딕셔너리에 키 , 값을 설정해줄수도있음
print(cabinet)
del cabinet[20]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items()) # 쌍으로 출력

cabinet.clear()
print((cabinet))