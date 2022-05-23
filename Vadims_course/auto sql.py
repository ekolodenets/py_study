import random
from tqdm import tqdm
import psycopg2
import names
from time import sleep

conn = psycopg2.connect(dbname='test_db1',
                        user='postgres',
                        password='password',
                        host='localhost',
                        port='5432')

cursor = conn.cursor()

i_d = 'id serial primary key'

tab_1 = {'employees': f'{i_d}, employee_name varchar(50) not null',
         'salary': f'{i_d}, monthly_salary int not null',
         'employee_salary': f'{i_d}, employee_id int not null unique, salary_id int not null',
         'roles': f'{i_d}, role_name int not null unique',
         'roles_employee': f'{i_d}, employee_id int not null unique, role_id int not null,'
                           f'foreign key(employee_id) references employees(id),'
                           f'foreign key(role_id) references roles(id)'
         }


def tables():
    try:
        for _, e in enumerate(tab_1):
            create_query = f'create table {list(tab_1)[_]} ({tab_1[list(tab_1)[_]]});'
            cursor.execute(create_query)
            conn.commit()
    except:
        print('Already exist')


# employees = 70 строк
def fill_table_1():
    position_1 = tab_1[list(tab_1)[0]].split(',')[1].split(' ')[1]
    for _ in range(70):
        n = names.get_full_name()
        create_query = f"insert into {list(tab_1)[0]}({position_1}) values('{n}')"
        cursor.execute(create_query)
    conn.commit()


# salary = 15 строк
def fill_table_2():
    position_1 = tab_1[list(tab_1)[1]].split(',')[1].split(' ')[1]
    for _ in range(1000, 2600, 100):
        create_query = f"insert into {list(tab_1)[1]}({position_1}) values('{_}')"
        cursor.execute(create_query)
    conn.commit()


# employee_salary = 40 строк: - в 10 строк из 40 вставить несуществующие employee_id
def fill_table_3():
    position_1 = tab_1[list(tab_1)[2]].split(',')[1].split(' ')[1]
    position_2 = tab_1[list(tab_1)[2]].split(',')[2].split(' ')[1]
    emp = [_ for _ in range(1, 71)]
    no_emp = [_ for _ in range(71, 99)]
    random.shuffle(emp)
    random.shuffle(no_emp)
    for _ in range(40):
        if _ < 30:
            create_query = f"insert into {list(tab_1)[2]}({position_1}, {position_2}) values({emp[_]},{random.randrange(1, 16)})"
            cursor.execute(create_query)
            conn.commit()
        else:
            create_query = f"insert into {list(tab_1)[2]}({position_1}, {position_2}) values({no_emp[_ - 30]},{random.randrange(1, 16)})"
            cursor.execute(create_query)
            conn.commit()


# roles = 20 строк, Поменять тип столба role_name с int на varchar(30)
def fill_table_4():
    positions = ['Junior Python developer',
                 'Middle Python developer',
                 'Senior Python developer',
                 'Junior Java developer',
                 'Middle Java developer',
                 'Senior Java developer',
                 'Junior JavaScript developer',
                 'Middle JavaScript developer',
                 'Senior JavaScript developer',
                 'Junior Manual QA engineer',
                 'Middle Manual QA engineer',
                 'Senior Manual QA engineer',
                 'Project Manager',
                 'Designer',
                 'HR',
                 'CEO',
                 'Sales manager',
                 'Junior Automation QA engineer',
                 'Middle Automation QA engineer',
                 'Senior Automation QA engineer']

    create_query = 'alter table roles alter column role_name type varchar(30) using roles::varchar(30);'
    cursor.execute(create_query)
    conn.commit()

    position_1 = tab_1[list(tab_1)[3]].split(',')[1].split(' ')[1]
    for _ in positions:
        create_query = f"insert into {list(tab_1)[3]}({position_1}) values('{_}')"
        cursor.execute(create_query)
    conn.commit()


# roles_employee = 40 строк
def fill_table_5():
    position_1 = tab_1[list(tab_1)[4]].split(',')[1].split(' ')[1]
    position_2 = tab_1[list(tab_1)[4]].split(',')[2].split(' ')[1]
    emp = [_ for _ in range(1, 41)]
    random.shuffle(emp)

    for i in emp:
        create_query = f"insert into {list(tab_1)[4]}({position_1}, {position_2}) values({i},{random.randrange(1, 21)})"
        cursor.execute(create_query)
        conn.commit()


# create 5 base tables
t = [tables(),
     fill_table_1(),
     fill_table_2(),
     fill_table_3(),
     fill_table_4(),
     fill_table_5()]

# loading through a beautifier
for _ in tqdm(t):
    _
    sleep(0.1) # to work more slowly
conn.close()
