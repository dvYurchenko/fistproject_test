#Самолет
import pickle
import json
class Plane:
    def __init__(self):
        # self.model = model
        # self.name = name
        # self.year = year
        # self.hight = hight
        # self.width = width
        # self.length = length
        # self.cruising_speed = cruising_speed
        # self.сapacity = сapacity
        self.my_dict = {}
        #self.my_list = []
    def add_dict(self):
        self.name = input('Введите название самолета: ')
        self.model = input('Введите название модели: ')
        self.year = input('Введите год выпуска: ')
        self.hight = input('Введите высоту: ')
        self.width = input('Введите ширину: ')
        self.length = input('Введите длину: ')
        self.cruising_speed = input('Введите крейсерскую скорость: ')
        self.capacity = input('Введите вместимость самолеты: ')
        self.my_dict[self.name] = {'model': self.model, 'year of release': self.year, 'hight': self.hight, 'width': self.width, 'length': self.length, 'сapacity': self.сapacity, 'cruising speed': self.cruising_speed}
        #self.my_list.append(self.my_dict)
    def show(self):
        return self.my_dict
    def menu(self):
        return "1. Посмотреть информацию \n 2. Добавить информацию \n 3. Упаковка/распаковка pickle \n 4. Упаковка/распаковка Json \n 0. Выход"
    def packaging(self):
        with open('data.pickle', 'wb') as file:
            pickle.dump(self.my_dict, file)
        with open('data.pickle', 'rb') as file:
            self.my_dict = pickle.load(file)
        print(pickle.dumps(self.my_dict))
    def packaging_json(self):
        with open('data_plane.json', 'w') as file:
            json.dump(self.my_dict, file, indent=2)
        with open('data_plane.json', 'r') as file:
            self.my_dict = json.load(file)
        print(json.dumps(self.my_dict, indent=2))

plane = Plane()

while True:
    print(plane.menu())
    value = int(input("Ваш выбор: "))
    if value == 1:
        print(plane.show())
    if value == 2:
        plane.add_dict()
    if value == 3:
        plane.packaging()
    if value == 4:
        plane.packaging_json()
    if value == 0:
        break
