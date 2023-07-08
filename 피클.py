# 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장

import pickle

profile_file = open("profile.pickle","wb") # b for binary
profile = {"이름":"박명수" , "나이":23, "취미":["농구","축구","야구"]} # 이렇게 딕셔너리형태에 리스트를 넣는것도 가능함
print(profile)
pickle.dump(profile,profile_file) # 프로필에있는 정보를 파일에 저장해줌
profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()