# Дан список целых чисел. Необходимо разработать метод sort_list(list), который
# поменяет местами все минимальные и максимальные элементы массива, а также
# добавит в конец массива одно минимальное значение из него.

# Тесты для примеров и проверки:
# sort_list([]) # => []
# sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
# sort_list([1]) # => [1, 1]
# sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]

def sort_list(list):
    if len(list) == 0:
        return list

    if len(list) == 1:
        list.append(list[0])
        return list

    min_value = min(list)
    max_value = max(list)
    result = [max_value if x == min_value else (min_value if x == max_value else x) for x in list]
    result.append(min_value)
    return result

