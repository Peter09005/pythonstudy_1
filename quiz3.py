#퀴즈3
string = "http://naver.com"
new_str = string[7:12]
count = new_str.count("e")
strLen = len(new_str)
password = new_str[0:3] + str(strLen) + str(count) + "!"
print(password)


# 이름을 주의해야겠다 str은 파이썬에서 형변환을 해줄때 쓰이므로 주의해서 쓰도록하자.