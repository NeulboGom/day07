#  Chapter 10 객체와 클래스

#  Inheritace
#  Parent Class, Super Class, Base Class 가 부모 클래스의 여러 명칭
#  Child Class, Sub Class, Derived Class 가 자식 클래스의 여러 명칭

'''class Car:
    pass

class Yugo(Car):
    pass

issubclass(Yugo,Car)        #  부모 자식 관계의 클래스가 맞는지 True False로 반환

class Car():
    def exclaim(self):  #  method
        print("I'm a car!")

class Yugo(Car):
    pass

Car().exclaim()
Yugo().exclaim()



#  Method Override  부모가 가진 메서드를 자식 클래tm에서 재정의하는 것

class Car():
    def exclaim(self):  #  method
        print("I'm a car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

Car().exclaim()
Yugo().exclaim()

print('='*60)
#  __init__을 포함한 모든 메서드를 오버라이드 할 수 있다.

class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self,name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person=Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")

print(person.name,doctor.name,lawyer.name)

print('='*60)
#  메서드 추가하기 - 부모 클래스에 없는 메서드를 자식 클래스에 추가 가능: 부모는 해당 메서드 이용 불가

class Car():
    def exclaim(self):  #  method
        print("I'm a car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")


# Car().exclaim()
# Yugo().exclaim()
# Yugo().need_a_push()
# Car().need_a_push()
print('='*60)

'''
#  super() 부모에게 도움 받기 // Override 사용

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성:",end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for skill in self.skills:
            print(skill)

    # def attack(self,idx):                     #    아래에서 Override 됐기 때문에 그냥 안 써도 될 듯
    #     print(f"{self.skills[idx]} 공격 시전")


class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self,idx):                       #  자식 클래스 Pikachu의 Override
        print(f"{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!")

pi1 = Pikachu('한지우',"50만 볼트/100만 볼트/번개")
# pi1.info()

class Ggoboogi(Pokemon):    #inhertance
    def __init__(self,owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self,idx):                       #  자식 클래스 Ggoboogi의 Override
        print(f"{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!")

    def swim(self):                     #  Ggoboogi 객체들이 사용할 수 있는 고유 스킬
        print(f"{self.name}가 수영을 합니다.")

Ggo1=Ggoboogi("오바람", "고속 스핀/거품/몸통박치기/하이드로펌프")
# Ggo1.info()

pi1.attack(0)
Ggo1.attack(2)

# p0=Pokemon("아이리스","스피드 스타/아이언 테일/지진/돌떨구기")
# p0.attack(0)
Ggo1.swim()
#pi1.swim()
