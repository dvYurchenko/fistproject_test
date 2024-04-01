#Лямбда-функции (функции для которых используется следующий синтаксис)
#lambda parametes:expression
# Где:
# parametes - переменные через запятую
# expression - условие, в которых нельзя использовать операторы или циклы, только условные выражения,
# нельзя вызывать return!
# Результатом выполнения лямбда-выражения является анонимная функция, при вызове которой вычисляется значение при указанных параметрах
# Например:
#Пример 1
x = 1
string = lambda x: 'k' if x == 1 else 's'
print(x)

#Пример 2
def area(b, h):
    return 0.5*b*h
area(6, 5)
area2 = lambda b,h: 0.5*b*h
print(area(6, 5))
print(area2(5, 6))

#Пример 3
elements = [(2, 12, 'Mg'), (1, 12, 'Arg'), (1, 3, 'Li'), (2, 4, 'Be')]
elements.sort(key=lambda e: (e[0], e[2]))
print(elements)
#elements.sort(key=lambda e: (e[1:3]))
elements.sort(key=lambda e: (e[2].lower(),e[1]))
print(elements)

#Пример 4
c = lambda x=1, y=2, z=3: x+y+z
print(c(5,3)) #Работа с параметрами

#Пример 5
y = lambda: 2+3
print(y()+y()) #аргументы указывать не обязательно

#Встроенные функции
list1 = [0,1,2,3,4,5,6,7,8]
list2 = list(filter(lambda x: x%3 == 0, list1))
print(list2)
#Filter принимает 2 аргумента: функцию и список для дальнейшей работы
list3 = list(map(lambda x: x%3 == 0, list1))
print(list3)
#map - вернет логическое (True, False) значение выражения для каждого компонента в пределах списка
from functools import reduce
list4 = reduce(lambda x,y: y-x, list1)
print(list4)
#reduce - выбирает в качестве аргументов списка первые 2 значения, выполняет операцию и
#возвращает значение по операции на следующий виток цикла до завершения списка (сводит элементы последовательности к
# одному значению, принимает 2 аргумента: функцию и список)
def add(x, y):
    return x+y
sum = reduce(add, list1)
print(sum)


