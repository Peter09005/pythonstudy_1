# score_file = open("score.txt","w",encoding="utf-8")
# print("수학 :0",file=score_file)
# print("국어 :100",file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf-8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()

score_file = open("score.txt","r",encoding="utf-8")
print(score_file.readline()) #한줄을 읽기
print(score_file.readline()) #그다음줄을 읽기
score_file.close

#read는 줄바꿈 자동으로 됨 하기 싫으면 end = ""

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

lines = score_file.readlines() # 리스트 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()