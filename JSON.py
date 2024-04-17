#Работа JSON в пайтон
import datetime
import json
data = {'name':'Jane', 'age':27, 'city': 'Perm'}

#Преобразование объекта Пайтон в строку JSON
json_data = json.dumps(data, indent=4, sort_keys=True)
print(json_data)
#dumps - преобразует словарь в строку в формате json
#indent - параметр отступа в строке
#sort_keys - сортировка ключенй в json
json_data = '{"name":"Jane", "age":27, "city": "Perm"}'
data = json.loads(json_data) #преобразование из строки в формате json в объект пайтон
print(type(data))
print(data['name'])

### Запись контейнера json в файле
with open('data.json', 'w') as file:
    json.dump(data, file)
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)

#Параметр default
import datetime
def datetime_serializer(x):
    #isinstance - проверяет существование объекта в классах, объявленных в пайтон

    if isinstance(x, datetime.datetime):
        return datetime.date.today().isoformat()
        #return x.strftime('%Y-%m-%d')

data = {"name":"Jane", "age":27, "city": "Perm", "birthday":datetime.datetime.now()}
json_data = json.dumps(data, indent=4, default=datetime_serializer)
print(json_data)

#Пользовательсктй класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_dict(person):
    return {"name":person.name, "age":person.age}
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return {"name":person.name, "age":person.age}
        return super().default(o)

person = Person("Alex", 33)
print(json.dumps(person, default=person_to_dict))
print(json.dumps(person, cls=JSONEncoder))
print()

#Параметр skipkeys
data = {(1, 2):"tuple_key", "normal_key":"value"}
print(json.dumps(data, skipkeys=True))
print()

#Практика
class Artical:
    def __init__(self, name, autor, col, editor, descript):
        self.name = name
        self.autor = autor
        self.col = col
        self.editor = editor
        self.descript = descript
        self.list = []
    def my_append(self, my_art):
        self.list.append(my_art)
        with open('artical.json', 'w') as file:
            json.dump(self.list, file, default=articalc_to_dict, indent=4)
        with open('artical.json', 'r') as file:
            self.list = json.load(file)
        print(json.dumps(self.list, indent=4))

def articalc_to_dict(artical):
    return {"name": artical.name, "autor": artical.autor, "number of characters": artical.col, "name of editor": artical.editor, "description": artical.descript}

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Artical):
            return {"name": artical.name, "autor": artical.autor, "number of characters": artical.col, "name of editor":artical.editor, "description": artical.descript}
        return super().default(o)

artical = Artical("Voina and Mir", "Lev Tolstoi", "5033", "Eksmo", "War and Peace is a historical novel by Leo Tolstoy first published serially in 1865 – 1869.")
artical.my_append(artical)
artical_1 = Artical("Carlson", "Astrit Lindren", "500", "Eksmo", "War and Peace is a historical novel by Leo Tolstoy first published serially in 1865 – 1869.")
artical_1.my_append(artical_1)

# with open('artical.json', 'w') as file:
#     json.dump(artical, file, default=articalc_to_dict, indent=4)
# with open('artical.json', 'r') as file:
#     artical = json.load(file)
# print(json.dumps(artical, indent=4))

#print(json.dumps(artical, default=articalc_to_dict))
#print(json.dumps(artical, cls=JSONEncoder))
print()




