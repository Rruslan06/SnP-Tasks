# Анаграмма — литературный приём, состоящий в перестановке букв или звуков
# определённого слова (или словосочетания), что в результате даёт другое слово
# или словосочетание.
# Разработайте метод combine_anagrams(words_array), который принимает на вход
# массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
# значения при определении анаграмм.

# Тест для примеров и проверки:
# combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
# "creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"],
# ["potatoes"], ["creams", "scream"] ]


def combine_anagrams(words):
    anag_words = {}
    for word in words:
        sort_element = "".join(sorted(word.lower()))
        if sort_element in anag_words:
            anag_words[sort_element].append(word)
        else:
            anag_words[sort_element] = [word]
    return list(anag_words.values())


