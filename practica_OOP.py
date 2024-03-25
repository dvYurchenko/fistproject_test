# Задание 1 (добавка к газировке)
class Soda:
    def __init__(self, dobavka=None):
        self.dobavka = dobavka

    def show_my_drink(self):
        if type(self.dobavka) == str:
            return (f"Газировка {self.dobavka}")
        else:
            return (f"Обычная газировка")


drink1 = Soda()
drink2 = Soda('Малина-лайм')
drink3 = Soda(5)
print(drink1.show_my_drink())
print(drink2.show_my_drink())
print(drink3.show_my_drink())
print('')


# Задание 2 (существование треугольника)
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) == int and type(self.b) == int and type(self.c) == int:
            if self.a > 0 and self.b > 0 and self.c > 0:
                if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.b + self.a:
                    return ('Ура, можно построить треугольник!')
                else:
                    return ('Жаль, но из этого треугольник не сделать.')
            else:
                return ('С отрицательными числами ничего не выйдет!')
        else:
            return ('Нужно вводить только числа!')


triangle = TriangleChecker(3, 4, 5)
print(triangle.is_triangle())
triangle = TriangleChecker(3, -4, 5)
print(triangle.is_triangle())
triangle = TriangleChecker('треугольник', -4, 5)
print(triangle.is_triangle())
triangle = TriangleChecker(1, 2, 3)
print(triangle.is_triangle())
print('')


#Задание 3
class Nikola:
    __slots__ = ['name', 'age'] #магический атрубут для ограничения свойств и методов в экземпляре
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.name == 'Николай':
            self.name = f'{self.name}, мне {self.age} года'
            print(self.name)
        else:
            self.name = f'Я не {self.name}, я Николай'
            print(self.name)

nikola = Nikola('Николай', 32)
nikola = Nikola('Максим', 32)
print('')

#Задание 4
# class RealString:
#     def __init__(self):
#         self.stroka_1 = ''
#         self.stroka_2 = ''
#     def inputInfo(self):
#         self.stroka_1 = str(input('Введите первую строку:'))
#         self.stroka_2 = str(input('Введите вторую строку:'))
#     def dlina(self):
#         if len(self.stroka_1) > len(self.stroka_2):
#             print('Больше 1 строка')
#         elif len(self.stroka_1) < len(self.stroka_2):
#             print('Больше 2 строка')
#         elif len(self.stroka_1) == len(self.stroka_2):
#             print('Строки равны')
# stroki = RealString()
# stroki.inputInfo()
# stroki.dlina()

class RealString:
    def __init__(self, some_str):
        self.some_str = some_str
    def __eq__(self, str123):
        return len(self.some_str) == len(str123)
    def __len__(self):
        return len(self.some_str)

str1 = RealString('Шоколадка')
str2 = RealString('Шоколадка')
str3 = 'Яблоко'
print(str1 == str3)


# __eq__() для равенства ==
# __ne__() для неравенства !=
# __ lt__() для оператора меньше <
# __ le__() для оператора меньше или равно <=
# __gt__() для оператора больше >
# __ge__() для оператора больше или равно >=







