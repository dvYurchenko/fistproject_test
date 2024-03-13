class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        self.__second = 0
        self.__third = 0
        ExampleClass.counter += 1
    def setSecond(self, val):
        self. __second = val
    def __str__(self):
        return f"{self.__first}, {self.__second}, {self.__third}"


example1 = ExampleClass()
print(example1. __dict__, example1.counter)
example2 = ExampleClass(2)
print(example2. __dict__, example2.counter)
example2.setSecond(3)
example3 = ExampleClass(4)
example3.third = 5
print(example3. __dict__, example3.counter)
#преобразование объекта в строку
print(example3)

#Пример 2
class ExampleClass2:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example4 = ExampleClass2(3)

try:
    print("b=",example4.b)
except AttributeError:
    pass
try:
    print("a=",example4.a)
except AttributeError:
    pass

#Практика
class Human:
    def _init__(self):
        self.home = ''
        self.city = ''
        self.__tel = ''
        self.fio = ''
        self.data = ''
        self.country = ''
    def getTel(self):
        return self. __tel
    def getTel(self,tel):
        self. __tel = tel

    def inputInfo(self):
        self.fio = input('Введите ФИО:')
        self.city = input('Введите город:')
        self.home = input('Введите дом:')
        tel = input('Введите телефон:')
        self.getTel(tel)
        self.data = input('Введите дату рождения:')
        self.country = input('Введите страну:')
    def __str__(self):
        return f"Данные человека: \n {self.fio} \n {self.city} \n {self.home} \n {self.getTel()} \n {self.data} \n {self.country} \n"
listHuman = [Human() for i in range(2)]
for i in range(len(listHuman)):
    print('*'*11)
    print(f'Human {i+1}')
    listHuman[i].inputInfo()
    print(listHuman[i].__dict__)
    print(listHuman[i]. __tel)
#human1 = Human()
#human1.inputInfo()
#print(human1)












