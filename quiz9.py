class SoldOutError(Exception): # Execption은 파라미터가 아니라 클래스를 상속받는거임.
    pass


chicken = 10
waiting = 1
while(True):
    try:
        if chicken == 0 :
            raise SoldOutError
        print("[남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇마리 주문 하시겠습니까?"))
        if order < 1 and type(order) != "int":
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다")
        else:
            print("[대기번호 {0}] {1} 마리의 주문 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
    except SoldOutError as err:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")


