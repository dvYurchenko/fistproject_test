#Инкапсуляция
class Phone:
    number = "111-11-11"
    def print_number(self):
        print("Phone number: ", self.number)

my_phone = Phone()
my_phone.print_number()

#public - нет реализации синтаксиса
#protected - одно нижнее подчеркивание (защищенный идентификатор для реализации внутренних методов класса)
#private - два нижних подчеркивания

class Phone:
    username = 'Kate'
    __how_many_times_turned_on = 0
    def call(self):
        print('Ring-Ring!')
    def __turn_on(self):
        self.__how_many_times_turned_on+=1
        print("Times was turned on: ", self.__how_many_times_turned_on)
my_phone = Phone()
my_phone.call()
print("The username is", my_phone.username)

#Полиморфизм
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} year old")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} year old")
    def make_sound(self):
        print("Bark")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    print()

#Пример переопределения метода (перегрузка)
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am two-dimensional shape"
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self,lenght):
        super().__init__("Square") #обращение к классу-родителю
        self.lenght = lenght
    def area(self):
        return self.lenght**2
    def fact(self):
        return "Square have each angle equal to 90 degrees"
class Circl(Shape):
    def __init__(self, radius):
        super().__init__("Circl")  # обращение к классу-родителю
        self.radius = radius
    def area(self):
        return pi*self.radius**2

from math import pi
a = Square(4)
b = Circl(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

#перегрузка методов - создание методов с одним и тем же именем, но с разными типами аргументов в ПАЙТОНЕ НЕ ПОДДЕРЖИВАЕТСЯ!
#ПОЛИМОРФИЗМ - передача параметров и методов класса другого значения тела функций, что и в родительском классе, для того, чтобы создать
#единственную сущность (метод, оператор, объект) для представления различных типов в различных сценариях использования.




