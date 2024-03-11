#Задание 1
file = 'C:/Users/Little/Desktop/Юрченко Дарья/text_2.txt'
file_1 = 'C:/Users/Little/Desktop/Юрченко Дарья/text_3.txt'
#stream = open(file, mode='r', encoding=None)
#stream_1 = open(file_1, mode='r', encoding=None)

#line_1 = stream_1.readline()
#line = stream.readline()
#while line != '':
    #for ch in line:
        #words = ch.split()
empty_set = set()
with open(file_1,'r') as file_1:
    content = file_1.read()
    words = content.split()
    for word in words:
        empty_set.add(word)
with open(file,'r') as file:
    content = file.read()
    words = content.split()
    with open("fail_3.txt", 'w') as file_3:
        for word in words:
            if word not in empty_set:
                file_3.write(word + ' ')

#Задание 2
my_dict = {'Арвидас Сабонис' : 221,'Ральф Сэмпсон' : 224,'Яо Мин' : 229, 'Келвин Мерфи' : 175, 'Дэйна Баррос' : 178, 'Майкс Джордан' : 198, 'Коби Брайант' : 198}
print(my_dict)
while(True):
    print('Задание 1. Добавить данные о баскетболисте:')
    print('Задание 2. Удалить данные о баскетболисте:')
    print('Задание 3. Найти данные о баскетболисте:')
    print('Задание 4. Изменить данные о баскетболисте:')
    print('0-выход.')
    print('*'*11)
    value=int(input('Введите номер задания: '))
    if (value==1):
        def dobavlenie(value1, value2):
            my_dict2 = {value1 : value2}
            my_dict.update(my_dict2)  # перезапись на новые значения
            print(my_dict)
        value1 = input('Введите имя баскетболиста: ')
        value2 = input('Введите рост баскетболиста: ') 
        dobavlenie(value1, value2)
    if (value == 2):
        def udalenie(value3):
            del my_dict[value3]
            print(my_dict)
        value3 = input('Введите имя баскетболиста, которого нужно удалить: ')
        udalenie(value3)
    if (value == 3):
        def poisk(value4):
            print('Рост баскетболиста: ', my_dict.get(value4))
        value4 = input('Введите имя баскетболиста: ')
        poisk(value4)
    if (value == 4):
        def zamena(value5):
            for key in my_dict:
                if key == value5:
                    my_dict[key] = input('Введите рост баскетболиста')


        value5 = input('Введите имя баскетболиста: ')