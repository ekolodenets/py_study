# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#    1. На вход обменнику вводишь количество денег int.
#    2. На выходе в консоль выводится отввет в таком виде:
#                "Ты ввёл int (Валюта)"
#                "конвертированная сумма в USD = int"
#    3. Валюту пользователя определите сами.***

import os

kurs = 2.62
os.system("cls")
print(f"===================================================\nНа 27 января 2022 года курс USD составляет {kurs} BYN")
byn = input('Отдаем ')
try:
    byn = int(byn)
except:
    try:
        byn = float(byn)
        os.system("cls")
        print(
            f"===================================================\nНа 27 января 2022 года курс USD составляет {kurs} BYN\n"
            f"Отдаем {byn} BYN = {round((byn / kurs), 2)} USD получим\n===================================================")
    except ValueError:
        print('Ошибка ввода')
else:
    os.system("cls")
    print(
        f"===================================================\nНа 27 января 2022 года курс USD составляет {kurs} BYN\n"
        f"Отдаем {byn} BYN = {round((byn / kurs), 2)} USD получим\n===================================================")
