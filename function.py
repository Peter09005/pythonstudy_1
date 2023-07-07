#함수


def open_account():
    print("새로운 계좌가 생성되었습니다")

open_account()

def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(format(balance+money)))
    return  balance + money

balance = 1000;
money = deposit(balance,20)
print(money)

def withdraw(balance,money):
    if(money>balance):
        return "돈이 없는데?"
    else:
        return balance-money

print(withdraw(balance,200))

# return a,b 라고 설정할수있고 , 받는 변수를 a,b 로 설정하면 잘 받아짐.


