# При выполнении следующих упражнений помните, что при получении невалидных
# параметров, в том числе неправильных типов данных, код программы не должен
# ломаться и должен выдавать всегда какое-либо значение. Название классов и их
# методы должны соответствовать тем, которые представлены в описании задачи.
# __________________________
# Упражнение 11
# Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
# принимающим на вход name и calories (не обязательные параметры), а также двумя
# методами is_healthy (возвращает true при условии калорийности десерта менее
# 200) и is_delicious (возвращает true для всех десертов).

class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories


    #геттер и сеттер для name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value
        else:
            self._name = "Unknown dessert" #Пусть вернется неизвестный дессерт чем другой тип 

    #геттер и сеттер для calories
    @property
    def calories(self):
        return self._calories
    
    
    @calories.setter
    def calories(self, value):
        if type(value) in (int, float):
            self._calories = value
        else:
            self._calories = 0 #получен неправильный тип данных, поэтому делаем заглушку  из нуля чтобы не ломалосб
    
    def is_healthy(self):
        return self.calories < 200
    
    def is_delicious(self):
        return True
    
