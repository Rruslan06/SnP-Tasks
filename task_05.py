# Разработать метод date_in_future(integer), который вернет дату через integer дней.
# Если integer не является целым числом, то метод должен вывести текущую дату.
# Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
# 22:33:44'.

# Тесты для примеров и проверки:
# date_in_future([]) # => текущая дата
# date_in_future(2) # => текущая дата + 2 дня

from datetime import datetime, timedelta


def date_in_future(integer):
    data = datetime.now()

    if type(integer) != int:
        return data.strftime("%d-%m-%Y %H:%M:%S")
    
    delta = timedelta(days=integer)
    new_data = data + delta
    return new_data.strftime("%d-%m-%Y %H:%M:%S") 
    