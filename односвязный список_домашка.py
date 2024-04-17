#Задание 1
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def displey(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return  False
    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    def replase(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next

list = LinkedList()
while True:
    print('Задание 1. Добавить элемент в список:')
    print('Задание 2. Удалить элемент из списка:')
    print('Задание 3. Показать содержимое списка:')
    print('Задание 4. Проверить есть ли значение в списке:')
    print('Задание 5. Заменить значение в списке:')
    print('0-выход.')
    print('*'*11)
    value = int(input('Введите номер задания: '))
    if (value == 1):
        data = int(input('Введите число: '))
        list.append(data)
    if (value == 2):
        data = int(input('Введите число для удаления: '))
        list.remove(data)
    if (value == 3):
        list.displey()
    if (value == 4):
        value = int(input('Введите число для поиска: '))
        print(list.search(value))
    if (value == 5):
        old_value = int(input('Введите число для замены: '))
        new_value = int(input('Введите  новое число для удаления: '))
        list.replase(old_value, new_value)
    if (value == 0):
        break







