#
class Car:
    #init - конструктор класса для инициализации объекта класса
    def __init__(self, fuel, maxspeed):
        #self - указатель на экземпляр класса
        self.fuel = fuel
        self.maxspeed = maxspeed
    def refuel(self, amount):
        self.fuel+=amount
    def drive(self):
        if self.fuel > 0:
            print('Driving')
            self.fuel-=1
        else:
            print('No fuel')
#MAIN
polo = Car(20, 185)
mini = Car(10, 170)
beetle = Car(0, 150)
#вывод атрибутов объекта
print(f'Polo has {polo.fuel} of fuel')
#вызов функций объекта
polo.drive()
print(f'Mini has {mini.fuel} of fuel')
mini.drive()
print(f'Beetle has {beetle.fuel} of fuel')
beetle.drive()

beetle.refuel(20)
beetle.drive()
print(f'Beetle has {beetle.fuel} of fuel')