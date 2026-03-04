# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.

# Тесты для примеров и проверки:
# count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
# "canal": 1, "panama": 1, "plan": 1}
# count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}

def count_words(string):
    line_text = ''
    res = {}

    for symbols in string.lower():
        if symbols.isalpha():
            line_text += symbols
        else:
            line_text += ' '
            
    words = line_text.split()

    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1

    return res


