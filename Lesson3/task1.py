# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль

def func(var_1, var_2):
    try:
        result = int(var_1) / int(var_2)
    except ValueError:
        return "Ошибка"
    except ZeroDivisionError:
        return "На 0 делить нельзя! "
    return round(result, 4)
print(func(input("Введите первое число: "), input("Введите второе число: ")))
