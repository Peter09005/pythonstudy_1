# 중복이 안되고 순서가 없음

my_set = {1,2,3,4,3}
print(my_set)

java = {"유재석","김태호","김참직"}
python = set(["유재석","박명수"])

#교집합 (java,python) 둘 다 할 수있는 개발자
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java-python)
print(java.difference(python))

# python 할 줄 아는 사람 +
python.add("김태호")

print(python)

java.remove("김태호")

print(java)