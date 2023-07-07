from random import *

cnt = 0
customer_time = []
for i in range(50):
    boo = ''
    customer_time.insert(i,randrange(5,51))
    if 5<= customer_time[i] <= 15:
        cnt+=1
        boo = 'O'
    print("[{2}] {0}번째 손님 (소요시간) : {1}분".format(i+1,customer_time[i],boo))

print("총 탑승 승객:{0}분".format(cnt))

