def profile(name,age,main_lang):
    print("이름 :{0} 나이:{1} 주 사용언어: {2}"\
          .format(name,age,main_lang))

profile("유재석",20,"파이썬")

# 같은 학교 같은 학년 같은 반 을 듣는 사람
# Default 값

def profile_def(name,age=17,main_lang="python"):
    print("이름 :{0} 나이:{1} 주 사용언어: {2}"\
        .format(name,age,main_lang))
profile_def("유재석")
profile_def("김태호")