string = {'Type':'str', 'Value':'int'}
with open('file.txt','w') as f:
    f.write(repr(string))
string2 = open('file.txt','r')
print(repr(string2.read()))
class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f'Products Details:{self.name}, price:{self.price}'

pr = Products('aaa', 2500)
print(pr)

#Пример
import os
class CountryDict:
    def __init__(self, user_input = 0):
        self.data = {}
        self.new_capital = ''
        self.country = ''
        self.filename = ''
    def add_data(self, country, capital):
        self.data[country] = capital
    def remove_data(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print ('Такой страны нет!')
    def search_data(self, country):
        if country in self.data:
            return self.data[country]
        else:
            return ('Такой страны нет!')
    def edit_data(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            return ('Страна не найдена!')
    def save_data(self, filename):
        with open(filename, 'w') as f:
            f.write(repr(self.data))
    def load_data(self, filename):
        if os.path.exist(self.filename)
            with open(filename, 'r') as f:
                self.data = eval(f.read())
    def menu(self):
        value = input('Load file? Y/N')
        if value == 'Y':
            self.load_data()
        while True:
            print('Menu: \n 1. Add data, \n 2. Remove data, \n 3. Search data \n 4. Edit data, \n 5. Save data, \n 6. Load data, \n 7. Exit')
            print('*' * 11)
            self.user_input = int(input('You choice: '))
            if self.user_input == 1:
                self.country = input('New country: ')
                self.new_capital = input('New capital: ')
                self.add_data(self.country, self.new_capital)
            if self.user_input == 2:
                self.country = input('Input remove country: ')
                self.remove_data(self.country)
            if self.user_input == 3:
                self.country = input('Input country: ')
                self.search_data(self.country)
            if self.user_input == 4:
                self.country = input('Input country: ')
                self.new_capital = input('Input new capital: ')
                self.edit_data(self.country, self.new_capital)
            if self.user_input == 5:
                self.filename = 'coutry_capital_data.txt'
                self.load_data(self.filename)
            if self.user_input == 6:
                self.filename = 'coutry_capital_data.txt'
            if self.user_input == 7:
                break

country = CountryDict()
country.menu()
country.add_data('USA', 'Washington')
country.add_data('UK', 'London')
country.add_data('Russia', 'Moscow')

print(country.search_data('Russia'))

country.edit_data('USA', 'Boston')
print(country.search_data('USA'))

country.save_data('coutry_capital_data.txt')

country.load_data('coutry_capital_data.txt')
print(country.data)





