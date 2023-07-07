absent = [2,5] # 결석

no_book = [7] # 책을 안가져옴

for student in range(1,11) :
    if student in absent: # 만약 student가 absent에 있으면, continue:
        continue
    if student in no_book:
        print("수업을 그만한다 {0}는 교무실로 와".format(student))
        break
    print("{0}번은 책을 읽어봐".format(student))
