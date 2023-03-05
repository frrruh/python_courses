# Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

# em = EmailValidator() # None
# В самом классе реализовать следующие методы класса (@classmethod):

# get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

# Корректность строки email определяется по следующим критериям:

# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд.

# Также в классе нужно реализовать приватный статический метод класса:

# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

# Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно. 

from random import randint
from string import ascii_lowercase, ascii_uppercase, digits

class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + "_.@" #список разрешенных символов
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits + "_" #список разрешенных символов

    
    def __new__(cls, *args, **kwargs):
        return None
    
    @classmethod
    def get_random_email(cls):
        n = randint(4,20)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return "".join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + "@gmail.com"

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.EMAIL_CHARS):
            return False
        s = email.split('@')
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        
        if '.' not in s[1]:
            return False
        
        if email.count('..') > 0:
            return False
        return True
    
    @staticmethod
    def __is_email_str(email):
        return type(email) == str
