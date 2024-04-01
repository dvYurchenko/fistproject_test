<<<<<<< HEAD
=======
#Задание 1 (окружность, вписанная в квадрат)
>>>>>>> a1c2a3d948a2943611247571f134cf894265a14f
from math import pi
class Circle:
    def __init__(self, radius):
            self.radius = radius
    def area(self):
        return pi * self.radius**2
class Square:
    def __init__(self, lenght):
            self.lenght = lenght
    def area(self):
        return self.lenght**2
class CircleInSquare(Circle, Square):
    def __init__(self, radius):
        Circle.__init__(self,radius)
        Square.__init__(self, radius *2**0.5)
    def display_details(self):
           print(f"Circle radius: {self.radius}")
           print(f"Square lenght:{self.lenght}")
    def total_area(self):
        circle_area = Circle.area(self)
        square_area = Square.area(self)
        return circle_area, square_area
circle_in_square = CircleInSquare(5)
circle_in_square.display_details()
circle_area, square_area = circle_in_square.total_area()
print(f"Total area of the circle:{circle_area}")
<<<<<<< HEAD
print(f"Total area of the square:{square_area}")
=======
print(f"Total area of the square:{square_area}")
print('')

#Задание 2
class Wheels:
    def __init__(self, radius):
            self.radius = radius
    def auto_wheels(self):
        return (f'Колеса автомобиля радиусом {self.radius}')
class Doors:
    def __init__(self, col):
        self.col = col
    def auto_doors(self):
        return (f'Автомобиль имеет {self.col} двери')
class Engine:
    def __init__(self, capacity):
        self.capacity = capacity
    def auto_engine(self):
        return (f'Объем двигателя автомобиля {self.capacity}')
class Type:
    def __init__(self, body_style):
        self.body_style = body_style
    def auto_type(self):
        return (f'Тип кузова автомобиля {self.body_style}')
class Auto(Wheels, Doors, Engine, Type):
    def __init__(self, radius, col, capacity, body_style ):
        Wheels.__init__(self, radius)
        Doors.__init__(self, col)
        Engine.__init__(self, capacity)
        Type.__init__(self, body_style)
    def display_details(self):
        det_1 = Wheels.auto_wheels(self)
        det_2 = Doors.auto_doors(self)
        det_3 = Engine.auto_engine(self)
        det_4 = Type.auto_type(self)
        print(det_1)
        print(det_2)
        print(det_3)
        print(det_4)

my_auto = Auto(18, 4, 2.5, 'crossover')
my_auto.display_details()
print('')


#Задание 3 (домашние животные)
class Cat:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} year old")
        print(f"I am а {self.type} cat")
    def make_sound(self):
        print("Meow-meow")

class Dog:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} year old")
        print(f"I am а {self.type} dog")
    def make_sound(self):
        print("Bark-bark")

class Parrot:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    def info(self):
        print(f"I am a parrot. My name is {self.name}. I am {self.age} year old")
        print(f"I am а {self.type} parrot")
    def make_sound(self):
        print("Tweet-tweet")

class Hamster:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    def info(self):
        print(f"I am a hamster. My name is {self.name}. I am {self.age} year old")
        print(f"I am а {self.type}")
    def make_sound(self):
        print("Squeak-squeak")

cat1 = Cat("Kitty", 2.5, 'Maine Coon')
dog1 = Dog("Fluffy", 4, 'Sheepdog')
parrot1 = Parrot("Kesha", 11, 'Ara')
hamster1 = Hamster("Homa", 1.5, 'an ordinary hamster')

for animal in (cat1, dog1, parrot1, hamster1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    print('')
print('')

#Задание 4 (служащие)
class Employer:
    def __init__(self, name, salary, experience, position):
        self.name = name
        self.salary = salary
        self.position = position
        self.work_experience = experience
    def display_employee(self):
        return ('This is Emloyer class')

class President(Employer):
    def display_employee(self):
        return (f'Name of the employee {self.name} \n Position of the employee: {self.position} \n Work_experience of the employee {self.work_experience} \n Salaryof the employee {self.salary}')

class Manager(Employer):
    def display_employee(self):
        return (f'Name of the employee {self.name} \n Position of the employee: {self.position} \n Work_experience of the employee {self.work_experience} \n Salaryof the employee {self.salary}')

class Worker(Employer):
    def display_employee(self):
        return (f'Name of the employee {self.name} \n Position of the employee: {self.position} \n Work_experience of the employee {self.work_experience} \n Salaryof the employee {self.salary}')


president = President('Andrey Ivanov', 100000, '15 years', 'president')
manager = Manager('Svetlana Sergeeva', 50500, '9 years', 'manager')
worker = Worker('Denis Petrov', 35000, '3 years', 'worker')
print(president.display_employee(), '\n')
print(manager.display_employee(), '\n')
print(worker.display_employee(), '\n')
print('')

#Задание 5 (магические методы)
class Employer:
    def __init__(self, name, salary, experience, position, age):
        self.name = name
        self.salary = salary
        self.position = position
        self.work_experience = experience
        self.age = age
    def __str__(self):
        return ('This is Emloyer class')
    def __int__(self):
        return ('Age of Emloyer')

class President(Employer):
    def __str__(self):
        return (f'Name of the employee {self.name} \n Position of the employee: {self.position} \n Work_experience of the employee {self.work_experience} \n Salaryof the employee {self.salary}')
    def __int__(self):
        return (f'Age of emloyer {self.age}')
class Manager(Employer):
    def __str__(self):
        return (f'Name of the employee {self.name} \n Position of the employee: {self.position} \n Work_experience of the employee {self.work_experience} \n Salaryof the employee {self.salary}')
    def __int__(self):
        return (f'Age of emloyer {self.age}')
class Worker(Employer):
    def __str__(self):
        return (f'Name of the employee {self.name} \n Position of the employee: {self.position} \n Work_experience of the employee {self.work_experience} \n Salaryof the employee {self.salary}')
    def __int__(self):
        return (f'Age of amloyer {self.age}')

president = President('Andrey Ivanov', 100000, '15 years', 'president', 42)
manager = Manager('Svetlana Sergeeva', 50500, '9 years', 'manager', 37)
worker = Worker('Denis Petrov', 35000, '3 years', 'worker', 26)
print(president.__str__(),'\n', president.__int__(), '\n')
print(manager.__str__(),'\n',manager.__int__(), '\n')
print(worker.__str__(), '\n',worker.__int__(), '\n')
>>>>>>> a1c2a3d948a2943611247571f134cf894265a14f
