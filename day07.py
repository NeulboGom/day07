#  Chapter 10 객체와 클래스

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

    def __repr__(self):
        return f"사각형의 좌표는 x = {self.x}이고, y = {self.y} 입니다. 면적은 {self.get_area()} 입니다."

    def __add__(self, other):
        return f"길이의 합은 {self.length + other.length}, 넓이는 {self.width + other.width}이고, " \
               f"면적의 합은 {self.get_area() + other.get_area()}입니다"
        # return Rectangle(0,0,(self.width + other.width), (self.length + other.length))  #  각 사각형의 길이와 넓이를 합하고 곱해서 나온 면적


c1=Circle(100, 100, 10.0)
c2=Circle(50, 50, 2.0)
r1=Rectangle(100, 50, 5,2)
r2=Rectangle(70, 30, 10, 15)

print(r1)
print(r2)
print(r1+r2)        #  r1.add(r2)인데, + 연산자로 간단하게..

print('='*60)

# Magic Method 매직 메서드

# Magic Method 안 쓰고
class Word():
    def __init__(self,text):
        self.text = text

    def equals(self,word2):
        return self.text.lower() == word2.text.lower()

a=Word("ace")
b=Word("ACE")
c=Word("AcD")
print(a.equals(b))
print(a.equals(c))
print((b.equals(c)))


#Magic Method 사용하면 .equals 없이 바로 비교 가능 다만 =가 ==로 바뀌어야 함
class Word():
    def __init__(self,text):
        self.text = text

    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()

a=Word("ace")
b=Word("ACE")
c=Word("AcD")

print(a==b)
print(b==c)
print(a==c)


# 나머지 도형의 부피 면적 비교해서 출력하는거 맹가보자


#  Aggregation and Composition
