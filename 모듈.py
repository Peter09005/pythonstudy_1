# 필요한것끼리 잘 만들어진 파일 >> C언어에서의 헤더와 비슷하네

import theater_module
theater_module.price(3)
theater_module.price_morning(4)

import theater_module as mv # 이건 mysql 과 유사하네
mv.price(4)
mv.price_morning(4)

from theater_module import *
# from random import * 과 비슷함 이렇게되면 theater_module 에 있는 모든 함수를 이용할수있다 > * 의 뜻이 모두 쓰겠다라는 뜻

# from theater_module import price > 이렇게 쓴다면 , price 함수밖에 이용하지 못함 당연한말..

from theater_module import price_morning as price # 라고 한다면
price(4)