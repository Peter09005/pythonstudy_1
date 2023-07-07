# 출석번호 1,2,3,4 >> 101, 102 , 103

students = [1,2,3,4,5]

students = [i+100 for i in students] # students에 있는 값을 가져와서 , i+100을 해준다.

print(students)

# 학생이름을 길이로 변환

students_name = ["황규태","김구","피카피카피카츄"]

students_len = [len(i) for i in students_name] # students에서 값을 가져와서 , len(i)를 해준뒤 리스트에 저장한다.

print(students_len)

students_upper = [i.upper() for i in students_name] #대문자이긴한데 한글이라서 잘 안나오는 모습 ^^..
print(students_upper)