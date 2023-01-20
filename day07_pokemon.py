#  super() 부모에게 도움 받기 // Override 사용

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성:",end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for idx in range(len(self.skills)):
            print(f"{idx+1} : {self.skills[idx]}")

        # for skill in self.skills:
        #     print(f'{skill}')

    # def attack(self,idx):                     #    아래에서 Override 됐기 때문에 그냥 안 써도 될 듯
    #     print(f"{self.skills[idx]} 공격 시전")


class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self,idx):                       #  자식 클래스 Pikachu의 Override
        print(f"{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!")

# pi1 = Pikachu('한지우',"50만 볼트/100만 볼트/번개")
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

class Firary(Pokemon):
    def __init__(self,owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self,idx):                       #  자식 클래스 Ggoboogi의 Override
        print(f"{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전!")


while True:
    menu = input("1) 포켓몬 생성 2) 프로그램 종료 : ")
    if menu == '2':
        print("프로그램을 종료합니다.")
        break
    elif menu == "1":
        pokemon = input("1) 피카츄 2) 꼬북이 3) 파이리")
        if pokemon == "1":
            owner = input("이름을 입력해주세요:")
            skills = input("사용 가능한 기술 입력('/'로 구분하여 입력):")
            p=Pikachu(owner, skills)
        elif pokemon == "2":
            owner = input("이름을 입력해주세요:")
            skills = input("사용 가능한 기술 입력('/'로 구분하여 입력):")
            p = Ggoboogi(owner, skills)
        elif pokemon == "3":
            owner = input("이름을 입력해주세요:")
            skills = input("사용 가능한 기술 입력('/'로 구분하여 입력):")
            p = Firary(owner, skills)
        else:
            print("포켓몬을 골라주세요.")
        while True:
            info_attack = input("1) 정보 조회 2) 공격 3) 종료:")
            if info_attack == '1':
                p.info()
            elif info_attack == '2':
                p.info()
                attack_menu = input("기술을 선택해 주세요:")
                p.attack(int(attack_menu)-1)
            elif info_attack == '3':
                break
            else:
                print("메뉴를 선택해 주세요")
    else:
        print("메뉴에서 골라 주세요.")


# Ggo1=Ggoboogi("오바람", "고속 스핀/거품/몸통박치기/하이드로펌프")
# # Ggo1.info()
#
# pi1.attack(0)
# Ggo1.attack(2)
#
# # p0=Pokemon("아이리스","스피드 스타/아이언 테일/지진/돌떨구기")
# # p0.attack(0)
# Ggo1.swim()
# #pi1.swim()

