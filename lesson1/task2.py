# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

time = int(input("Введите время в секундах: "))
day = time // 86400
hours = time // 3600 - day * 24
minutes = time // 60 - hours * 60
minutes = minutes % 60
seconds = time % 60
if day >= 1: print(f"{day:} days {hours:02}:{minutes:02}:{seconds:02}")
else: print(f"{hours:02}:{minutes:02}:{seconds:02}")