for i in range(1,51):
    fileName = str(i) + "주차.txt"
    with open (fileName,"w",encoding = "utf-8") as fileWrite:
        fileWrite.write("-{0}주차 보고서\n".format(i))
        fileWrite.write("부서:\n")
        fileWrite.write("이름:\n")
        fileWrite.write("업무 요약:\n")