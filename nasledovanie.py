#Наследование

class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
class Sub(Super):
    def __init(self, name):
        Super.__init__(self, name)
obj = Sub("Andrey")
print(obj)

#пример 3х уровнего наследования
class Level1:
    varial1 = 100
    def __init__(self):
        self.var1 = 101
    def fun1(self):
        return 102
class Level2(Level1):
    varial2 = 200
    def __init__(self):
        Level1.__init__(self)
        self.var2 = 201
    def fun2(self):
        return 202
class Level3(Level2):
    varial3 = 300
    def __init__(self):
        self.var3 = 301
        Level2.__init__(self)
    def fun3(self):
        return 302
obj = Level3()
print(obj.varial1, obj.var1, obj.fun1())
print(obj.varial2, obj.var2, obj.fun2())
print(obj.varial3, obj.var3, obj.fun3())

#Множественное наследование
class SuperA:
    varA = 10
    def funA(self):
        return 11
class SuperB:
    varB = 20
    def funB(self):
        return 13
class Sub(SuperA, SuperB):
    pass
obj = Sub()
print(obj.varA, obj.funA())
print(obj.varB, obj.funB())

#одинаковые атрибуты и функции
class Left:
    var = "L"
    varLeft = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    varRight = "RR"
    def fun(self):
        return "Right"
class Sub(Left, Right):
    pass
class Sub2(Right,Left):
    pass
obj = Sub()
print(obj.var, obj.varLeft, obj.varRight, obj.fun())
obj1 = Sub2()
print(obj1.var, obj1.varLeft, obj1.varRight, obj1.fun())
#Внутри самого класса-наследника
# В суперклассе, снизу вверх

#иерархия классов
class One:
    def doit(self):
        print("doit from One")
    def doanything(self):
        self.doit()
class Two(One):
    def doit(self):
        print("doit from Two")
one = One()
two = Two()
one.doanything()
two.doanything()

