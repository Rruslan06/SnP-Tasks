# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.

# Тест для примеров и проверки:
# multiply_numbers() # => None
# multiply_numbers('ss') # => None
# multiply_numbers('1234') # => 24
# multiply_numbers('sssdd34') # => 12
# multiply_numbers(2.3) # => 6
# multiply_numbers([5, 6, 4]) # => 120


def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    
    res = 1
    flag = False

    inputs = str(inputs)
    for symbol in inputs:
        if symbol.isdigit():
            res *= int(symbol)
            flag = True
    
    return res if flag else None

