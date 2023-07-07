a = input("숫자를 입력하세요") # input을 통해 값을 받아올수있다.
if a > 10 :
    print("10보다 큰 수")
elif a < 10:
    print("10보다 작은 수")
else:
    print("10입니다")


if a > 10 or a < 10 :
    print("10입니다")

temp =  int(input("기온은 어때요"))

if a > 30 :
    print("너무 덥습니다")
elif a>10 and a<30:
    print("괜찮은 날씨입니다")
elif 0 <= a <= 10: # 이런식으로도 조건을 걸어줄수있다.
    print("조금 춥습니다")
