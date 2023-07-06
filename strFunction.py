python = "Python is Amazing";
print(python.lower()); #소문자로 만들어줌
print(python.upper()); #대문자로 만들어줌
print(python.isupper()); #앞자리가 upper이냐? True False
print(len(python)); #길이를 알려준다.
print(python.replace("Python","Java"));
print("BAD! > 바꾼뒤 : "+python); # 그냥 str의 값을 가져와서, java로 바꾼 새로운 string을 만들어서 return해주는함수인듯..

index = python.index("n");
print(index); #처음나오는 문자의 값을 알려준다
index = python.index("n",index+1); # index+1 을 파라미터로 주게되면 index+1번째 부터 찾기 떄문에 이렇게 하면 다음 "n"의 index값을 반환한다.
print(index);

print(python.find("n")); # 이것도 비슷한 함수임
print(python.find("Java")); # return -1 만약 있냐/ 없냐 를 구분해야하는 함수를 만들려면, find를 써야한다.

print(python.count("n")) # n이 몇번 포함되어있나.