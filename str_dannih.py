#Структуры данных
#1) Bytearray
a = bytearray((12, 7, 5, 3, 5))
print(a)
print(a[1])
print(a[0])
a.append(30)
print(a)
#Принимает числа в диапазоне [0; 256]

#2) Счетчик (Counter)
from collections import Counter
print(Counter(['A', 'A', 'B', 'C', 'C', 'B', 'B', 'A', 'C']))
counter = Counter({'A': 3, 'B': 6, 'C': 2})
print(counter)
counter.update(['A',1])
counter.update(['B',2])
print(counter)

#DefaultDict
from collections import defaultdict
dict1 = defaultdict(int)
list1 = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 9]
for i in list1:
    dict1[i] += 1
print(dict1)

#ChainMap
from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
c = ChainMap(d1, d2, d3)
print(c)
print(c['a'])
print(c['f'])
print('')

#Связанный список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
list = LinkedList()
list.head = Node(1)
second = Node(2)
third = Node(3)
#связываем элементы
list.head.next = second
second.next = third
#обход элементов
list.printList()
print('')

#Стек списком
stack = []
stack.append('g')
stack.append('v')
stack.append('c')
print('Реализация стека: ', stack)
print('Удаление элементов из стека: ')
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print('Стек очищен!')
print('')

#стек коллекцией
from collections import deque
stack = deque()
stack.append('g')
stack.append('v')
stack.append('c')
print('Реализация стека: ', stack)
print('Удаление элементов из стека: ')
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print('Стек очищен!')
print('')

#стек с использованием модуля очереди
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
print(stack.qsize())

stack.put('g')
stack.put('c')
stack.put('s')

print('Весь стек: ', stack.full())
print('Размер стека: ', stack.qsize())
#Освобождение стека
print(stack.get())
print(stack.get())
print(stack.get())
#Проверка на пустоту
print(stack.empty())
print('')

#Очередь с приоритетом
class VipQueue(object):
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self, data):
        self.queue.append(data)
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
myQueue = VipQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(17)
print(myQueue)
while not myQueue.isEmpty():
    print(myQueue.delete())
    print(myQueue)

#Практика
spisok = []
for i in range(10):
    spisok.append(input('Введите число: '))
print(spisok)
while(True):
    print('Задание 1. Добавить новое число в список:')
    print('Задание 2. Удалить все вхождения числа из списка:')
    print('Задание 3. Показать содержимое списка:')
    print('Задание 4. Проверить есть ли значение в списке:')
    print('Задание 5. Заменить значение в списке:')
    print('0-выход.')
    print('*'*11)
    value = int(input('Введите номер задания: '))
    if (value == 1):
        value = input('Введите число: ')
        for i in range(len(spisok)):
            if spisok[i] == value:
                print(f'Число {value} уже есть в списке')
            elif value not in spisok:
                spisok.append(value)
        print(spisok)
    if (value == 2):
        value = input('Введите число: ')
        for i in range(len(spisok)):
            if value in spisok:
                spisok.remove(value)
        print(spisok)
    if (value == 3):
        while (True):
            print('Задание 1. Список нужно показать с начала:')
            print('Задание 2. Список нужно показать с конца:')
            print('0-выход.')
            print('*' * 11)
            value = int(input('Введите номер задания: '))
            if (value == 1):
                print(spisok)
            if (value == 2):
                print(spisok[::-1])
            if (value == 0):
                break
    if (value == 4):
        value = input('Введите число: ')
        if value in spisok:
            print(f'Значение {value} есть в списке')
        else:
            print(f'Значения {value} нет в списке')
    if (value == 5):
        while (True):
            print('Задание 1. Заменить только первое вхождение:')
            print('Задание 2. Заменить все вхождения:')
            print('0-выход.')
            print('*' * 11)
            value = int(input('Введите номер задания: '))
            if (value == 1):
                value = input('Введите число: ')
                value_1 = input('Введите число для замены: ')
                for i in range(len(spisok)):
                    if spisok[i] == value:
                        spisok[i] = value_1
                        print(spisok)
                        break
            if (value == 2):
                value = input('Введите число: ')
                value_1 = input('Введите число для замены: ')
                for i in range(len(spisok)):
                    if spisok[i] == value:
                        spisok[i] = value_1
                print(spisok)
            if (value == 0):
                break
    if (value == 0):
        break

















