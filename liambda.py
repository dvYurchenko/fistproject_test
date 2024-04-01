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

#Пример 2
def area(b, h):
    return 0.5*b*h
area(6, 5)
area2 = lambda b,h: 0.5*b*h
print(area2(5, 6))

#Пример 3
elements = [(2, 12, 'Mg'), (1, 11, 'Na'), (1, 3, 'Li'), (2, 4, 'Be')]
elements.sort(key=lambda e: (e[1], e[2]))
print(elements)
elements.sort(key=lambda e: (e[1:3]))
#elements.sort(key=lambda e: (e[2].lower(),e[1]))
print(elements)

