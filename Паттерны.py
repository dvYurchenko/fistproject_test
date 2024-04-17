#Паттерны проектирования
#Singleton

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'): #проверяем атрибут instance
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Объект создан", s)
s1 = Singleton()
print("Объект создан", s1)

#Отложенный Singleton
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__method called...")
        else:
            print("Instance already created: ", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
s = Singleton()
print("Объект создан: ", Singleton.getInstance())
s1 = Singleton()

#Моностатический Singleton
class Borg:
    __shared__state = {"1": "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared__state
        pass

b = Borg()
b1 = Borg()
b.x = 4
print("Borg object 'b': ", b)
print("Borg object 'b1': ", b1)
print("object state 'b': ", b.__dict__)
print("object state 'b1': ", b1.__dict__)

#Singleton и метаклассы
#Метакласс - это классы, экземплярами которых являются классы.

class MyInt(type):
    def __call__(cls, *args, **kargs):
        print("Here's my int", args)
        print("")
        return type.__call__(cls, *args, **kargs)
class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
i = int(4, 5)

#Пример использования
class HealthCheck:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck.__instance:
            HealthCheck.__instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck.__instance
    def __init__(self):
        self._servers = []
    def addServers(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    def changeServers(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()
hc1.addServers()

print("Schedule health check for servers(1)...")
for i in range(4):
    print("Checking", hc1._servers[i])

hc2.changeServers()
print("Schedule health check for servers(2)...")
for i in range(4):
    print("Checking", hc2._servers[i])




