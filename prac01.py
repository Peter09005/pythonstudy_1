# boolean
# not TRUE -> FALSE

# 변수 전역 , 지역

name = '연탄'
print(name+'입니다');

# 자료형 str(age) int(str) 이렇게 바꿔줄수있음

# 위에서 선언한 변수를 아래에서 다시 바꿔주면 변수가 덮어쓰기된다.

# + 가 아닌 , 로도 문자열을 합할수가있다. , 는 굳이 문자열 변환을 안해줘도 된다. ,은 띄어쓰기가 반드시 포함이 되기때문에 아주 자유롭진 않은것같다.

# 주석 ctrl + /
'''
이것도 주석처리입니다.
'''

#연산자
print(2**3); #2의3승 c언어에서는 math 헤더를 추가했어야했는데 걍 개꿀이네.
print(2%5);
print(5/2); #자동으로 형변환이된다.
print(5//2); #몫도 나온다.

#abs 절댓값
neg = -2;
pos = abs(neg);
print(pos);
print(pow(pos,pos));
print(max(pos,neg));
print(round(pos*0.23));

from math import *
print(floor(3.9)) # 내림
print(ceil(3.14)) # 천장 올림
print(sqrt(4.2)) # 제곱근


#랜덤함수

from random import *
i = random()
print(i)
print(randrange(1,45)) # 1부터 44 까지 int 자료형으로 return해줌
print(int(random()*45)) # 위 코드와 정확히 똑같음
print(randint(1,45)); # 이렇게 해주주면 1부터 45, randrange함수는 1부터 n-1까지였지만. 