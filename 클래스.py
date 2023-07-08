# Class

name = "마린"
hp = 40
dmg = 5

# 살짝 구조체랑 비슷하네

tank_name = "tank"
tank_hp = 150
tank_dmg = 30

def attack(name , location, dmg):
    print("{0}이/가 {1}방향으로 {2}만큼의 데미지를 줍니다".format(name,location,dmg))
# 너무 귀찮고 , 매번 이렇게 하는건 비효율적임 >> 틀을 이미 만든뒤 , 틀을 사용하는게 좋겠다!

class Unit:
    def __init__(self,name,hp): # 생성자: 초기화 시켜주는거임 클래스를 시작할떄 name, hp , dmg를 받아서 초기화를 야무지게 시켜줌 자바랑 똑같네 그냥
        self.name = name # 멤버변수 >> class내에서 정의된 변수
        self.hp = hp
        print("{0}유닛이 생성되었습니다".format(self.name))
class AttackUnit(Unit):
    def __init__(self,name,hp,dmg):
        Unit.__init__(self,name,hp)
        self.dmg = dmg
    def attack (self,location):
        print("{0}:{1}방향으로 {2} 만큼의 데미지로 공격합니다".format(self.name,location,self.dmg ))

    def damaged (self,damage):
        self.hp -= damage
        if self.hp > 0:
            print("{0}유닛이 {1}만큼의 데미지를 받았습니다. 현재 {0}의 체력 :{2}".format(self.name,damage,self.hp))
        else:
            print("{0}유닛은 죽었습니다".format(self.name))

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name,location):
        print("{0}: {1} 방향으로 날아갑니다 [속도:{2}] ".format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,dmg,flying_speed):
        AttackUnit.__init__(self,name,hp,dmg)
        Flyable.__init__(self, flying_speed)


# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack(5)
# firebat1.damaged(25)
# firebat1.damaged(25)

valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")


# 메소드 오버라이딩 >> 클래스안에서 재정의 한다.

# pass

class Building(Unit):
    def __init__(self,name,hp,location):
        super.__init__(name,hp)
        self.location = location

supply_depot = Building("서플라이디폿",500,"7시")

