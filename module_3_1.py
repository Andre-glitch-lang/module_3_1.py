"""
 [v]Создать переменную calls = 0 вне функций.
 [v]Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
 [v]Создать функцию string_info с параметром string и реализовать логику работы по описанию.
 [v]Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
 [v]Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
 [v]Вывести значение переменной calls на экран(в консоль).
"""
from pickletools import string1

global calls
calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    string1 = str(string)
    length = len(string1)
    string_2 = string1.upper()
    string_1 = string1.lower()
    string_sum = []
    string_sum.append(length)
    string_sum.append(string_2)
    string_sum.append(string_1)
    count_calls()
    return string_sum


def is_contains(sting, list_of_search):
    a = 0
    flag = True
    for i in list_of_search:
        string1 = sting.lower()
        list = i
        list = list.lower
        if string1 == list:
            a = a + 1
        if a >= 1:
            flag = True
        else:
            flag = flag
            count_calls()
            return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
