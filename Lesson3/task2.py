# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Осуществить вывод данных
# о пользователе одной строкой

def user_info(name, f_name, year, city, email, phone):
     return f"Имя - {name}, Фамилия - {f_name}, год рождения - {year}, " \
            f"Город проживания - {city}, email: {email}, telefon: {phone} "

print(user_info(name="Михаил", f_name="Даниленко", year="1980", city="Уфа",
                email="pred@mail.ru", phone="41-09136"))
