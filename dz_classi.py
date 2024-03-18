#Автомобиль
class Auto:
    def __init__(self, model, marka, year, color, price, energi):
        self.model = model
        self.marka = marka
        self.year = year
        self.color = color
        self.price = price
        self.energi = energi
    def getInput(self):
        self.model = input('Введите название: ')
        self.marka = input('Введите марку автомобиля: ')
        self.year = input('Введите год автомобиля: ')
        self.color = input('Введите цвет автомобиля: ')
        self.price = input('Введите цену автомобиля: ')
        self.energi = input('Введите объем двигателя автомобиля: ')
        print(f'Операция выполнена! \n {"*" * 11}')
    def setInput(self, valueInput):
        if valueInput == 1:
            self.model = input('Введите название ')
        elif valueInput == 2:
            self.marka = input('Введите марку автомобиля ')
        elif valueInput == 3:
            self.year = input('Введите год автомобиля ')
        elif valueInput == 4:
            self.color = input('Введите цвет автомобиля ')
        elif valueInput == 5:
            self.price = input('Введите цену автомобиля ')
        elif valueInput == 6:
            self.energi = input('Введите объем двигателя автомобиля ')
        print(f'Операция выполнена! \n {"*"*11}')
    def __str__(self):
        return f"Название: {self.model} \n Марка: {self.marka} \n Год выпуска: {self.year} \n Цвет: {self.color} \n Цена: {self.price} \n Объем двигателя: {self.energi} \n"
    def menu(self):
        return "1. Посмотреть информацию \n 2. Дополнить информацию \n 3. Изменить данные \n 0. Выход"
    def menuInput(self):
        print(f"1. Название \n 2. Марка \n 3. Год выпуска \n 4. Цвет \n 5. Цена \n 6. Объем двигателя \n")
        valueInput = int(input("Ваш выбор: "))
        self.setInput(valueInput)


auto = Auto('Chevrole Aveo','Chevrole', '2016', 'green', '800000', '1.4')

while True:
    print(auto.menu())
    value = int(input("Ваш выбор: "))
    if value == 1:
        print(auto)
    if value == 2:
        auto.menuInput()
    if value == 3:
        auto.getInput()
    if value == 0:
        pass
        print('Приходите еще!!!')


