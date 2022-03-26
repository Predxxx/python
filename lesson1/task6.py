revenue = float(input("Введите значение выручки: "))
cost = float(input("Введите значение издержек: "))
result = revenue - cost
if result > 0:
    print(f"Ваша компания работает с прибылью {result}", "рублей")
    print(f"Ваша рентабельность составила {100 * result / revenue:1f}%" )
    n = int(input("Сколько сотрудников работает в Вашей компании: "))
    revenue_n = result / n
    print(f"На каждого Вашего сотрудника приходится: ", (revenue_n), "рублей прибыли")
elif result < 0:
    print(f"Ваша компания работает с убытком {result}", "рублей")
elif result == 0:
    print("В Вашей компании пока нет ни прибыли, ни убытка")