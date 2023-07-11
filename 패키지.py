# 많은 모듈을 하나에 모아둔걸 패키지라고 함

import travel.thailand # 클래스나 함수는 이렇게 import를 하지 못한다. >> from으로 해야한다.

trip_to = travel.thailand.ThailandPackage() # 객체 생성 했음
trip_to.detail()

from travel import vietnam
trip_to1 = travel.vietnam.VietnamPackage()
trip_to1.detail()

import inspect
import random
print(inspect.getfile(random)) # 이렇게 되면 random이 어디위치에 있는지 알려줌
print(inspect.getfile(travel.thailand))

# 내가 만든 패키지를 random이 위치한 파일안에 넣어두면 , 다른 프로젝트를 만들어도 거기에서도 똑같이 사용할수있음
# from random import * < 이런식으로 random은 패키지이고 , *은 모듈임

