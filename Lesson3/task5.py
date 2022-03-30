# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме

def sum_chis():
    s = 0
    while True:
        l = input("Введите число, или нажмите 'q' для выхода: ").split()
        for i in l:
            try:
                if i.lower() == 'q':
                    return s
                else:
                    s += int(i)
            except ValueError:
                print("Введите число, или нажмите 'q'")
        print(f"Сумма чисел {s}")


print(sum_chis())