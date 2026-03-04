import time
# Упражнение 13
# Напишите декоратор @cached, который кэширует результаты функции, чтобы
# избежать повторных вычислений для одних и тех же аргументов. Декоратор
# должен поддерживать:

# • ограничение размера кэша: при превышении максимально хранимого
# количества записей (max_size) удаляются самые старые записи:
# • если max_size=None, то размер кэша не ограничен
# • если max_size не соответствует целому числу, то также
# инициализировать его как None
# • время жизни записей: автоматически удалять результаты, сохранённые
# более seconds назад:
# • если seconds=None, то записи не устаревают
# • размер кэша не ограничен, если seconds не соответствует целому
# числу, то также инициализировать его как None
# • декоратор должен учитывать как позиционные (*args), так и
# именованные аргументы (**kwargs)

# 13

# Тесты для примеров и проверки:
# @cached(max_size=3, seconds=10)
# def slow_function(x):
# print(f"Вычисляю для {x}...")
# return x ** 2
# # Первый вызов — вычисляется
# print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
# # Повторный вызов с теми же аргументами — берётся из кэша
# print(slow_function(2)) # Вывод: 4 (без вычисления)
# # Через 15 секунд кэш устареет, и будет новое вычисление
# time.sleep(15)
# print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    def decorator(func):
        cache = {} 
        order = [] 

        def wrapper(*args, **kwargs):
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__

            main_key = (args, tuple(kwargs.items()))
            stop = time.time()  

            if main_key in cache: #запись есть в кэше? (Да)
                
                if seconds is None or (stop - cache[main_key][1]) <= seconds: #Время истекло?(Нет)
                    return cache[main_key][0]
                
                else: #Время истекло?(Да)
                    res = func(*args, **kwargs)
                    cache[main_key] = (res, stop)
                    return res

            else: #запись есть в кэше? (Нет)
                
                if max_size is None or len(order) < max_size: #размер order превышен?(Нет)
                    order.append(main_key)
                    res = func(*args, **kwargs)
                    cache[main_key] = (res, stop)
                    return res

                else: #размер order превышен?(Да)
                    cache.pop(order[0])
                    order.pop(0)

                    order.append(main_key)
                    res = func(*args, **kwargs)
                    cache[main_key] = (res, stop)
                    return res

        return wrapper
    return decorator



