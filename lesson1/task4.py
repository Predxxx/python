#  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции


n = int(input("Введите целое положительное число:  "))
a = 0
b = n
c = 0
while b > 0:
    c = b % 10
    if c > a:
        a = c
        if a == 9:
            break
    b = b // 10
print(f"Самая большая цифра в числе {n} равна {a}")