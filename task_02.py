# Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
# range) для определения элементов из массива list, значения которого входят в
# указанный диапазон range. Если не передан хотя бы один из параметров, то
# должен вернуться пустой массив.

# Тесты для примеров и проверки:
# coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
# coincidence() # => []
# coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]

def coincidence(list=None, range=None):
    if list == None or range == None:
        return []
    result_list = []
    for i in list:
        if type(i) in (int, float):
            if range.start <= i < range.stop:
                result_list.append(i)
            else:
                continue
        else:
            continue
    return result_list

