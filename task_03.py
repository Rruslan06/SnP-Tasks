# Дан список элементов произвольной природы. Необходимо разработать метод
# max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
# тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
# переданном массиве.

# Тесты для примеров и проверки:
# max_odd([1, 2, 3, 4, 4]) # => 3
# max_odd([21.0, 2, 3, 4, 4]) # => 21
# max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
# max_odd(['ololo', 'fufufu']) # => None
# max_odd([2, 2, 4]) # => None

def max_odd(array):
    answer = None

    def depth_ver(i):
        nonlocal answer

        if type(i) is list:
            for deep_i in i:
                depth_ver(deep_i)
            return
    
        if type(i) not in (int, float):
            return
        elif type(i) == float and not i.is_integer():
            return
        else:
            item = int(i)

        if  item % 2 != 0:
            if answer is None or item > answer:
                answer = item
            else: 
                return

    for i in array:
        depth_ver(i)
    
    return answer


