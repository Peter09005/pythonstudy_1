print("Python","Java",sep=",")
#seperate > , 로 바뀐다.
print("Python","Java",sep="vs")
print("Python","Java",end="?")
print("무엇이 더 재미있을까요?")
#end의 의미 문장의 끝을 물음표로 바꿔준다 원래는 Enter였지만 , ? 로 출력된다

import sys
#print("Python","Java",file=sys.stdout)
#표준출력

score = {"수학":90,"영어":50,"코딩":100}
for subject,score in score.items():
    print(subject.ljust(8),str(score).rjust(4),sep=":")
    #진짜 별게 다 있네.. rjust , ljust 같은 기능이있다. 정렬할때 아주 유용할듯

#대기순번표 1 > 001 2 > 002 이렇게 설정할수있다.

for num in range(1,21):
    print("대기번호:" + str(num).zfill(3))

#표준 입력

answer = input("아무값이나 입력하세요")
# input 에서 return 된값은 항상 string으로 나온다.
answer = int(input("아무값이나 입력하세요"))


