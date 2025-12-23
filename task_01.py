# Разработайте метод is_palindrome(string), который будет определять, является ли
# параметр string палиндромом (строкой, которая читается одинаково как сначала
# так и с конца), при условии игнорирования пробелов, знаков препинания и
# регистра.

def is_palindrome(string):
    if string == None:
        return False
    
    s = str(string).lower()
    only_letter = ""

    for i in s:
        if i.isalnum():
            only_letter += i
    
    return s == s[::-1]
