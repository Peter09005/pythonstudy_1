# with 를 통해 파일 입출력 편하게 할수있음

import pickle

with open("profile.pickle","rb") as profile_file: # profile.pickle을 rb로 연다. 접근은 profile_file이 한다. 종료 필요 X
    print(pickle.load((profile_file)))

with open("study.txt","w",encoding="utf-8") as studyFile:
    studyFile.write("수학: 100 점 ")

with open("study.txt","r",encoding="utf-8") as studyFile:
    print(studyFile.read())