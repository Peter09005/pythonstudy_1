from random import *
idSet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("-- 당첨자 발표 --")
shuffle(idSet)
print("치킨당첨자"+str(idSet[0])+"\n")
idSet.remove(idSet[0])
print(sample(idSet,3))


users = range(1,21) # 1부터 20까지 숫자를 생성 class > range
users = list(users)
