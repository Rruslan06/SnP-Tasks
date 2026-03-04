# Разработать методы для программы Камень-Ножницы-Бумага. При реализации
# обработки исключений важно не использовать встроенные классы ошибок с
# передачей им сообщения, а разработать классы с представленными ниже
# названиями.

# Метод rps_game_winner должен принимать на вход массив следующей структуры
# [ ["player1", "P"], ["player2", "S"] ], где P — бумага, S — ножницы, R — камень, и
# функционировать следующим образом:
 
# • если количество игроков больше 2 необходимо вызывать исключение
# WrongNumberOfPlayersError
# • если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
# исключение NoSuchStrategyError
# • в иных случаях необходимо вернуть имя и ход победителя, если оба
# игрока походили одинаково - выигрывает первый игрок.

# Тесты для примеров и проверки:
# rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #
# => WrongNumberOfPlayersError
# rps_game_winner([['player1', 'P'], ['player2', 'A']]) #
# => NoSuchStrategyError
# rps_game_winner([['player1', 'P'], ['player2', 'S']]) #
# => 'player2 S'
# rps_game_winner([['player1', 'P'], ['player2', 'P']]) #    
# => 'player1 P'


class WrongNumberOfPlayersError(Exception):
    """Неверное количество игроков"""
    pass

class NoSuchStrategyError(Exception):
    """Нет такого хода в игре"""
    pass

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError
    
    (name1, move1), (name2, move2) = game

    if move1  not in ('R','P','S') or move2 not in ('R','P','S'):
        raise NoSuchStrategyError
    
    rules = {
        "R": "S",
        "S": "P",
        "P": "R"
    }

    if move1 == move2 or rules[move1] == move2:
        return f'{name1} {move1}'
    
    return f'{name2} {move2}'


