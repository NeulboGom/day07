#  Chapter 10 객체와 클래스

# self == 실행되는 시점의 객체 or
# class name.function(객체 이름)

# 속성 접근

# 직접 접근
'''class Duck:
    def __int__(self, input_name):
        self.name = input_name

fowl=Duck("Daffy")
fowl.name

# 직접 접근:
fowl.name = "Daphne"
fowl.name
'''

# Getter, Setter 메서드 // 캡슐화 - 굳이 외부에 공개할 필요가 없는 것은 감추자 // 약한 결합
# private으로 선언된 것을 이용할 수 있는 방법.

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):     #  getter
        print("Inside the getter")
        return self.hidden_name
    def set_name(self, input_name):     #  setter
        print("Insdie the setter")
        self.hidden_name = input_name
    #name=property(get_name,set_name)

don = Duck("Donald")
don.get_name()
don.set_name("Donna")

# 이거 다시 공부해야함 하나도 이해 못하고 제대로 출력도 안됨 - 자습시간 활용

# Class and Object Attribute 클래스와 객체 속성

class Fruit:
    color='red'     #Class 속성 // self.머시기는 instance 속성 // self는 객체 명을 위한...

blueberry=Fruit()
print(Fruit.color)
print(blueberry.color)

print('='*60)

blueberry.color='blue'
print(Fruit.color)
print(blueberry.color)
# Fruit 의 color를 바꾸면 그 이후에 생성되는 객체들은 바뀐 색으로 지정

# Method Type 메서드 타입 // 다시 공부하자



# Duck typing


# *Polymorphism  ex) 도형의 면적을 구하는 함수를 만들고, 삼각형, 사각형, 원에 따라서 알아서 처리, but 도형이여야 함

#도형을 이용한 예제

import math


class Shape():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_area(self):
        print("도형의 면적을 출력합니다.")


class Circle(Shape):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius)**2

class Cylinder(Circle):
    def __init__(self,x,y,radius,height):
        super().__init__(x,y,radius)
        self.height = height

    def get_area(self):
        return super().get_area() * self.height

class Rectangle(Shape):
    def __init__(self,x,y,width,length):
        super().__init__(x,y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


c1=Circle(100, 100, 10.0)
c2=Circle(50, 50, 2.0)
r1=Rectangle(100, 50, 5,2)

print(f"{c1.get_area()} // {c2.get_area()} // {r1.get_area()}")
print(f"사각형의 좌표는 x = {r1.x}이고, y = {r1.y} 입니다. 면적은 {r1.get_area()} 입니다.")
print(f"원1의 좌표는 x = {c1.x}이고, y = {c1.y} 입니다. 면적은 {c1.get_area()} 입니다.")

cyl1=Cylinder(100, 100, 10.0,2)
print(f"원기둥의 좌표는 x = {cyl1.x}이고, y = {cyl1.y} 입니다. 부피는은 {cyl1.get_area()} 입니다.")
