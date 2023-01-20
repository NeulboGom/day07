#  Chapter 10 객체와 클래스

#  Multiple Inheritance - 다중 상속 // 여러 부모 클래스로부터 상속받는 것

# 형태
# class Mule(Donkey, Horse): -> Donkey, Horse, Animal 순서로 첫 번째, 두 번째, 세 번째 부모 클래스가 정해짐
#       psss

class Animal:
    def says(self):
        return "I speak!"


class Horse(Animal):
    def says(self):
        return "Neigh!"

class Donkey(Animal):
    def says(self):
        return "Hee-Haw"

class Snake(Animal):
    def says(self):
        return "Ssss-sss"

class Mule(Donkey,Horse,Snake):
    pass

class Hinny(Snake,Horse,Donkey):
    pass
    # def says(self):
    #     return "버새가 웁니다."

m1=Mule()
h1=Hinny()
print(h1.says())            #  Horse 먼저
print(m1.says())            #  Donkey 먼저
"""만약 Donkey와 Horse의 says가 전부 없으면 Animal로 감 // 둘 중에 하나만 남으면 하나 남은 걸로 감 // 다만 순서는 위에 적힌 대로"""

#Method Resolution Order
print(Mule.mro())  #  실행하면 부모 순서대로 나옴 / 자기 자신 - 1부모 - 2부모 - 3부모
print(Hinny.mro())

# Mixin 믹스인: 클래스 정의에 부모 클래스를 추가하여 상속 받을 수 있다. 다만 Helper의 목적으로만
# 다른 상위 클래스와 Method를 공유하지 않음 /
# Mixin 클래스는 부모클래스가 되지 않으면서 어떤 클래스에서 사용할 수 있는 메소드를 포함하는 클래스입니다.
# 다시 한번, Mixin은 상속의 개념으로 쓰는 것이 아니라 끼워넣는 개념에 가깝습니다.
# 믹스인이란 클래스에서 제공해야 하는 추가적인 메서드만 정의하는 작은 클래스를 말합니다.
# 믹스인 클래스는 자체의 인스턴스 속성(attribute)를 정의하지 않으며 __init__ 생성자를 호출하도록 요구하지 않습니다.

class PrettyMixin():
    def time_print(self):
        import datetime
        print(datetime.datetime.now())
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t=Thing()
t.name="Nyarlathoep"
t.feature="ichor"
t.age="Eldritch"
t.gender="Female"
t.dump()
t.time_print()


