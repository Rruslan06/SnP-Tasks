# Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
# переданных словаря, значениями ключей в которых являются числа, и вернет
# новый словарь, полученный по следующим правилам:

# • приоритетными являются ключи того словаря, сумма значений ключей
# которого больше (если суммы значений ключей будут равны, то второй
# словарь считается более приоритетным)
# • ключи со значениями меньше 10 не должны попасть в финальный
# словарь
# • получившийся словарь должен вернуться упорядоченным по значениям
# ключей в порядке возрастания.

# Тесты для примеров и проверки:
# connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>
# { "c": 11, "b": 12 }
# connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
# { d: 11, "c": 12, "a": 13 }
# connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>
# { "c": 11, "b": 12, "a": 15 }

def connect_dicts(dict1, dict2):
    high_prior_dict, low_prior_dict = (dict1, dict2) if sum(dict1.values()) > sum(dict2.values()) else (dict2, dict1)
    general_dict = {**low_prior_dict, **high_prior_dict}
    filter_dict = {key: value for key, value in general_dict.items() if value >= 10}
    res = dict(sorted(filter_dict.items(), key=lambda i: i[1]))
    return res

