def std_weight(height,gender):
    height_meter = height/100
    if gender == "남자":
        return (height_meter**2)*22
    else:
        return (height_meter**2)*21

gender = input("성별 입력 ")
height = int(input("키 입력 "))

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height,gender,round(std_weight(height,gender)),2))