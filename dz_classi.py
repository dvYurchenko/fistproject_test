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
        break
<<<<<<< HEAD
print('Приходите еще!!!')
=======
        print('Приходите еще!!!')

#Книги
class Book:
    def __init__(self, name, autor, year, edito, genre, price):
        self.name = name
        self.autor = autor
        self.year = year
        self.editor = edito
        self.genre = genre
        self.price = price
    def getInput(self):
        self.name = input('Введите название книги: ')
        self.autor = input('Введите автора книги: ')
        self.year = input('Введите год выпуска: ')
        self.editor = input('Введите издателя: ')
        self.genre = input('Введите жанр: ')
        self.price = input('Введите цену: ')
        print(f'Операция выполнена! \n {"*" * 11}')
    def setInput(self, valueInput):
        if valueInput == 1:
            self.name = input('Введите название книги ')
        elif valueInput == 2:
            self.autor = input('Введите автора книги ')
        elif valueInput == 3:
            self.year = input('Введите год выпуска ')
        elif valueInput == 4:
            self.editor = input('Введите издателя ')
        elif valueInput == 5:
            self.genre = input('Введите жанр ')
        elif valueInput == 6:
            self.price = input('Введите цену ')
        print(f'Операция выполнена! \n {"*"*11}')
    def __str__(self):
        return f"Название книги: {self.name} \n Автор: {self.autor} \n Год выпуска: {self.year} \n Издатель: {self.editor} \n Жанр: {self.genre} \n Цена: {self.price} \n"
    def menu(self):
        return "1. Посмотреть информацию \n 2. Дополнить информацию \n 3. Изменить данные \n 0. Выход"
    def menuInput(self):
        print(f"1. Название книги \n 2. Автор \n 3. Год выпуска \n 4. Издатель \n 5. Жанр \n 6. Цена \n")
        valueInput = int(input("Ваш выбор: "))
        self.setInput(valueInput)


book = Book('War and Peace','Lev Tolstoy', '1865', 'AST Press', 'Novel', '1000')

while True:
    print(book.menu())
    value = int(input("Ваш выбор: "))
    if value == 1:
        print(book)
    if value == 2:
        book.menuInput()
    if value == 3:
        book.getInput()
    if value == 0:
        break
        print('Приходите еще!!!')

#Стадион
class Stadium:
    def __init__(self, name, year, coutry, city, capacity):
        self.name = name
        self.year = year
        self.coutry = coutry
        self.city = city
        self.capacity = capacity
    def getInput(self):
        self.name = input('Введите название стадиона: ')
        self.year = input('Введите дату открытия: ')
        self.coutry = input('Введите страну: ')
        self.city = input('Введите город: ')
        self.capacity = input('Введите вместимость: ')
        print(f'Операция выполнена! \n {"*" * 11}')
    def setInput(self, valueInput):
        if valueInput == 1:
            self.name = input('Введите название книги ')
        elif valueInput == 2:
            self.year = input('Введите дату открытия ')
        elif valueInput == 3:
            self.coutry = input('Введите страну ')
        elif valueInput == 4:
            self.city = input('Введите город ')
        elif valueInput == 5:
            self.capacity = input('Введите вместимость стадиона ')
        print(f'Операция выполнена! \n {"*"*11}')
    def __str__(self):
        return f"Название стадиона: {self.name} \n Дата открытия: {self.year} \n Страна: {self.coutry} \n Город: {self.city} \n Вместимость: {self.capacity} \n"
    def menu(self):
        return "1. Посмотреть информацию \n 2. Дополнить информацию \n 3. Изменить данные \n 0. Выход"
    def menuInput(self):
        print(f"1. Название стадиона \n 2. Дата открытия \n 3. Страна \n 4. Город \n 5. Вместимость \n")
        valueInput = int(input("Ваш выбор: "))
        self.setInput(valueInput)


stadium = Stadium('Dinamo','1925', 'Russia', 'Perm', '3000')

while True:
    print(stadium.menu())
    value = int(input("Ваш выбор: "))
    if value == 1:
        print(stadium)
    if value == 2:
        stadium.menuInput()
    if value == 3:
        stadium.getInput()
    if value == 0:
        break
        print('Приходите еще!!!')
>>>>>>> ef7a0519d60641c3a8ef1f2141b6b8012510d07d


