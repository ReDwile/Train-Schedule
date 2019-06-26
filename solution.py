from functions import *
import os
import shutil

name = 'renfe.csv' # Имя файла с данными

# Подгружаем функции
upload_data(name)
sorting_data()

path = os.getcwd() + '/tickets'
try: # При повторном запуске обновляются данные
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)

for country_key in tickets.keys(): # Сохраняет данные из tickets в память компьютера
    name = 'tickets/' + country_key + '.csv'
    with open(name, 'w') as f:
        f.write(f'Время отправления,Время прибытия,Тип поезда,Цена,Класс,Тип тарифа\n')
        for date_key in tickets[country_key].keys():
            for mas in tickets[country_key][date_key]:
                for i in range(len(mas) - 1):
                    f.write(f'{mas[i]},')
                f.write(f'{mas[-1]}\n')

while True:
    country_1 = input('Пункт отправления: ').lower()
    country_2 = input('Пункт прибытия: ').lower()
    if country_1 == '' or country_2 == '':
        break
    date = input('Введите дату отправления в формате ГГГГ-ММ-ДД: ')
    name = country_1 + '-' + country_2
    try:
        for mas in tickets[name][date]:
            string = '(' + country_1.upper() + ', ' + country_2.upper() + ', '
            for i in range(len(mas) - 1):
                string += str(mas[i]) + ', '
            string += mas[-1] + ')'
            print(string)
    except:
        print('Ошибка')