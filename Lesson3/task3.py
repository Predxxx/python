# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов

def my_func(var_1, var_2, var_3):
    l = [var_1, var_2, var_3]
    try:
        l.remove(min(l))
        return sum(l)
    except TypeError:
        return "Введите число"

print(my_func(18, 14, 28))

