# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

revenue = float(input("Введите значение выручки: "))
cost = float(input("Введите значение издержек: "))
result = revenue - cost
if result > 0:
    print(f"Ваша компания работает с прибылью {result}", "рублей")
elif result < 0:
    print(f"Ваша компания работает с убытком {result}", "рублей")
elif result == 0:
    print("В Вашей компании пока нет ни прибыли, ни убытка")