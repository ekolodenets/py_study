import csv
import random
import random as r
import time
import names
import os
from datetime import datetime


start_time = datetime.now()
def path(name: str):
    file_path = os.path.join(os.path.expanduser('~'), 'Desktop', name)  # link to user's desktop
    return file_path


# Python CSV
#
# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
#
print('Задание №1', end='')
# 1.Создать пустой empty.csv файл
with open(path('empty.csv'), 'w') as empty:
    pass
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №2', end='')
# 2.Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
with open(path('digits.csv'), 'w', newline='') as digits:
    writer = csv.writer(digits)
    for i in range(151):
        row = [i]
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №3', end='')
# 3.Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
with open(path('names.csv'), 'w', newline='') as names_:
    writer = csv.writer(names_)
    for i in range(100):
        row = [names.get_last_name()]
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №4', end='')
# 4.Вариант 1. Создать emails.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
with open(path('emails.csv'), 'w', newline='') as e_mails:
    writer = csv.writer(e_mails)
    for i in range(100):
        row = [f'{names.get_last_name().lower()}@gmail.com']
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №5', end='')
# 5.Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
with open(path('nne.csv'), 'w', newline='') as nne_:
    columns = ["Number", "Name", "Email"]
    writer = csv.DictWriter(nne_, fieldnames=columns)
    writer.writeheader()
    for i in range(1, 101):
        nam = names.get_last_name()
        em = f'{nam.lower()}@gmail.com'
        row = {"Number": i, "Name": nam, "Email": em}
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №6', end='')
# 6.Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
my_digits = [i for i in range(10, 311)]
with open(path('digits_2.csv'), 'w', newline='') as digits_2:
    columns = ["Number"]
    writer = csv.DictWriter(digits_2, fieldnames=columns)
    writer.writeheader()
    for i in my_digits:
        row = {"Number": i}
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №7', end='')
# 7.Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами
my_names = [names.get_last_name() for _ in range(400)]
with open(path('names_2.csv'), 'w', newline='') as names_2:
    columns = ["Name"]
    writer = csv.DictWriter(names_2, fieldnames=columns)
    writer.writeheader()
    for i in my_names:
        row = {"Name": i}
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №8', end='')
# 8.Вариант 2. Создать emails_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com
add = '@gmail.com'
my_emails = [(i.lower()+add) for i in my_names]
with open(path('emails_2.csv'), 'w', newline='') as emails_2:
    columns = ["Email"]
    writer = csv.DictWriter(emails_2, fieldnames=columns)
    writer.writeheader()
    for i in my_emails:
        row = {"Email": i}
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №9', end='')
# 9.Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
add = '@gmail.com'
get_names = [names.get_last_name() for i in range(450)]
get_mails = [i.lower()+add for i in get_names]

with open(path('nne_2.csv'), 'w', newline='') as nne_2:
    columns = ["Number", "Name", "Email"]
    writer = csv.DictWriter(nne_2, fieldnames=columns)
    writer.writeheader()
    for i, v in enumerate(get_names):
        row = {"Number": i+1, "Name": get_names[i], "Email": get_mails[i]}
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №10', end='')
# 10.Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# 	a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# 	b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# 	с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# 	в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)

date_all = [random.randrange(1980, 1990) for _ in range(50)] + [random.randrange(1991, 2000) for _ in range(100)] + \
           [random.randrange(2001, 2010) for _ in range(150)] + [random.randrange(2011, 2021) for _ in range(150)]

# одновременное открытие двух файлов и работа с ними + создание нового файла для сохранения
# with open(path('nne_2.csv'), 'r') as f_in, open(path('nne_2..csv'), 'w', newline='') as f_out:
#     csv_reader = csv.reader(f_in)
#     columns = ["Number", "Name", "Email", "Date"]
#     writer = csv.DictWriter(f_out, fieldnames=columns)
#     writer.writeheader()
#     for i, row in enumerate(csv_reader):
#         if i != 0 and i != 450:
#             x = {"Number": row[0], "Name":row[1], "Email":row[2], "Date":date_all[i]}
#             writer.writerow(x)

# поочередное открытие двух файлов и работа с ними
listing = []
with open(path('nne_2.csv'), 'r') as f_in:
    reader = csv.DictReader(f_in)
    for i, e in enumerate(reader):
        e["Date"] = date_all[i]
        listing.append(e)

with open(path('nne_2.csv'), 'w', newline='') as f_out:
    columns = ["Number", "Name", "Email", "Date"]
    writer = csv.DictWriter(f_out, fieldnames=columns)
    writer.writeheader()
    for i, row in enumerate(listing):
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print('\rЗадание №11', end='')
# 11.Создать файл combo.csv с полями Name, Email, Date. 1000 строк.
# 	a) Соберите имена из файла nne_2.csv.
# 	b) недостающие 550 строк имён сгенерируйте.
# 	с) Имена расположите в алфавитном порядке.
# 	d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# 	e) Остальные даты генерировать рандомно.
# 	f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

def phone():
    first = str(r.randint(100, 999))
    second = str(r.randint(1, 888)).zfill(3)
    last = (str(r.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(r.randint(1, 9998)).zfill(4))
    return f'{first}-{second}-{last}'


gender = ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female',
          'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'mix']

listing = []
with open(path('nne_2.csv'), 'r') as f_in:
    reader = csv.DictReader(f_in)
    for i in reader:
        i.pop("Number")
        listing.append(i)

list_1 = []
for i, v in enumerate(listing):
    v["Phone"] = phone()
    v["Gender"] = random.choice(gender)
    v["Salary"] = random.randrange(1000, 10000, 500)
    list_1.append(v)

list_2 = []
for i in range(550):
    dic = dict()
    dic["Name"] = names.get_last_name()
    dic["Email"] = dic["Name"].lower() + '@gmail.com'
    dic["Date"] = random.randrange(1980, 2022)
    dic["Phone"] = phone()
    dic["Gender"] = random.choice(gender)
    dic["Salary"] = random.randrange(1000, 10000, 500)
    list_2.append(dic)

list_1000 = list_1 + list_2
list_1000 = sorted(list_1000, key=lambda item: item.get("Name"))
for i, v in enumerate(list_1000):
    v['Number'] = i+1

with open(path('combo.csv'), 'w', newline='') as combo:
    columns = ["Number", "Name", "Email", "Date", "Phone", "Gender", "Salary"]
    writer = csv.DictWriter(combo, fieldnames=columns)
    writer.writeheader()
    for i, row in enumerate(list_1000):
        writer.writerow(row)
print(f' готово', end='')
time.sleep(0.5)

print(f'\rВремя выполнения запроса - {datetime.now() - start_time}')

# P.S.
# Задания специально написаны немного запутанно)) Привыкайте.
# Реализация и порядок выполнения каждого задания и внутренних подпунктов заданий любая, особенно в 10 и 11 задании. )) Главное чтобы работало.
