
# 빈자리는 빈공간 , 오른쪽 정렬 , 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일떄는 + , 음수일떄는 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

print("{0:_<+10}".format(500))

print("{0:,}".format(10000000000))

print("{0:+,}".format(1000000000000))

print("{0:^<+30,}".format(10000000))

print("{0:f}".format(5/3))

print("{0:.2f}".format(5/3))