jumin = "990120-1234567";

print("성별:"+jumin[7]);

# index로 str 접근가능.

print("연"+jumin[0:2]); #0부터2번째 직전값까지 0~1까지 가져온다.

# 애초에 배열이 그렇지 arr[8] 까지 설정해도 arr[7]까지밖에 못 입력하잖아

print(jumin[:6]); #처음부터 6 직전까지
print(jumin[7:]); #7부터 끝까지

print(jumin[-1]) #index의 마지막 번호는 -1 번째이다. 따라서 7을 가져오려면 jumin[-1] >> 편하긴한데..