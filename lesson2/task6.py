# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть
# характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя

goods = []
for i in range(1, 4):
    print(f"Заполняем информацию по {i}-му товару")
    name = input("Название: ")
    price = int(input("Цена: "))
    count = int(input("Количество: "))
    measure =  input("Единица измерения: ")
    goods.append((i, {"название": name, "цена": price, "количество": count, "eд": measure}))


print(*goods, sep='\n')


names = []
prices = []
counts = []
measures = []

for i in goods:
    names.append(i[1].get("название"))
    prices.append(i[1].get("цена"))
    counts.append(i[1].get("количество"))
    measures.append(i[1].get("eд"))

report = {
    "название": list(set(names)),
    "цена": list(set(prices)),
    "количество": list(set(counts)),
    "eд": list(set(measures))
}

print(f'{report}')