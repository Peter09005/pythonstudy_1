
try:
    print("나누기 전용 계산기");
    nums = []
    nums.append(int(input("첫번쨰 숫자:")))
    nums.append(int(input("두번째 숫자:")))
    # nums.append(int(nums[0]/ nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError: # 문제가 발생했을떄 , except 을 보고 만약 해당되는 에러를 찾으면 , 아래 코드를 실행한다.
    print("에러")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
