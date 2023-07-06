# 리스트 []

subway = [10,20,30]

a = subway.pop(2)
print(a)

print(subway)

subway = ["유재석","조세호","장미란"]
print(subway.index("조세호")) # index로 "조세호" 가 어디있는지 알려준다

# 하하씨가 다음 정류장에서 다음 칸에 탐

subway.append("하하")

print(subway)

subway.insert(1,"정형돈") # index 1번에 넣는다

print(subway)

subway.pop() # pop을 하면 뒤쪽부터 꺼내줌
subway.pop() # 리스트는 stack 기반인가?

print(subway)

# 중복된 값을 가진 index가 몇개인지

subway.append("유재석")
print(subway.count("유재석"))

# 정렬

num_list = [1,3,5,2,3,2,5,7,8,4]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

# 리스트는 자료형에 구애 X 섞어서 쓸수있다

mix_list = ["조세호",2,3,5,1]

# 리스트 확장

num_list.extend(mix_list)

print(num_list)