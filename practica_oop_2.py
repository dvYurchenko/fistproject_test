class Programmer:
    def __init__(self, name, position, salary, time):
        self.name = name
        self.position = position
        self.salary = salary
        self.time = time
        self.hourly_rate = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def work(self, time):
        self.time += time
        self.salary += self.time*self.hourly_rate[self.position]
    def rise(self):
        if self.position == 'Junior':
            if self.hourly_rate[self.position] >= 15:
                self.position = "Middle"
            else:
                self.hourly_rate[self.position] += 1
        elif self.position == 'Middle':
            if self.hourly_rate[self.position] >= 20:
                self.position = "Senior"
            else:
                self.hourly_rate[self.position] += 1
    def info(self):
        return (f'{self.name}, количество отработанных часов: {self.time}, накопленная зарплата: {self.salary}, должность: {self.position}')

programmer = Programmer('Васильев Иван', 'Junior', 10, 0)
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.work(250)
programmer.rise()
print(programmer.info())
programmer.work(250)
programmer.rise()
print(programmer.info())
programmer.work(250)
programmer.rise()
print(programmer.info())

#Задание 2
from random import randint
class NPC:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def __str__(self):
        return (f'Имя: {self.name}. Очки здоровья: {self.points}')
class Swordsman(NPC):
    def attact(self, min_att, max_att):
        a = randint(min_att, max_att)
        return (f'Мечник {self.name} нанес {a}')
class Mag(NPC):
    def attact(self, mana):
        if mana > 0:
            mana_1 = mana*2
            return (f'Маг {self.name} нанес {mana_1} урона')
        else:
            return ('Не могу атаковать')

npc = Swordsman('Гендельф', 100)
npc2 = Mag('Кот Пушистик', 20)
print(npc)
print(npc.attact(2,10))
print(npc2.attact(0))

















