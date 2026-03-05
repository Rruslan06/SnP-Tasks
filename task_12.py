# При выполнении следующих упражнений помните, что при получении невалидных
# параметров, в том числе неправильных типов данных, код программы не должен
# ломаться и должен выдавать всегда какое-либо значение. Название классов и их
# методы должны соответствовать тем, которые представлены в описании задачи.

# Упражнение 11
# Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
# принимающим на вход name и calories (не обязательные параметры), а также двумя
# методами is_healthy (возвращает true при условии калорийности десерта менее
# 200) и is_delicious (возвращает true для всех десертов).

# Упражнение 12
# Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
# геттером и сеттером для атрибута flavor (все параметры являются не
# обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
# false только в тех случаях, когда flavor равняется «black licorice».

class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories


    #геттер и сеттер для name
    @property
    def name(self):
        return self._name
    
    @name.setter #на всякий и его сделаем принимающим все
    def name(self, value):
        self._name = value


    #геттер и сеттер для calories
    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, value):
            self._calories = value #Теперь принимает любой тип
    
    def is_healthy(self):
        if isinstance(self._calories, (int, float)) and self._calories < 200: #Проверяем что если число и менее калорийное, то гуд
            return True
        else:
            return False
    
    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self._flavor 
    
    @flavor.setter
    def flavor(self, value):
        self._flavor = value


    def is_delicious(self):
        if self._flavor != "black licorice":
            return super().is_delicious()
        else:
            return False