# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# * Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_
# type_list.
#
# В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
#
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
# через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
import os
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    regex_prod = re.compile('Изготовитель системы')
    regex_name = re.compile('Название ОС')
    regex_code = re.compile('Код продукта')
    regex_type = re.compile('Тип системы')

    for i in os.listdir():
        if i[0:4] == 'info':
            f = open(i, 'r')
            for i in f:
                if regex_prod.search(i):
                    i = i.rstrip().split(" - ")
                    os_prod_list.append(i[1])
                    continue
                if regex_name.search(i):
                    i = i.rstrip().split(" - ")
                    os_name_list.append(i[1])
                    continue
                if regex_code.search(i):
                    i = i.rstrip().split(" - ")
                    os_code_list.append(i[1])
                    continue
                if regex_type.search(i):
                    i = i.rstrip().split(" - ")
                    os_type_list.append(i[1])
                    continue
            f.close()
    i = len(os_prod_list) - 1
    while i >= 0:
        templist = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(templist)
        i -= 1
    return main_data


def write_to_csv(main_data):
    with open('main_data.txt', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(main_data)
    return

if __name__ == "__main__":
    write_to_csv(get_data())

# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
# скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
#
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = dict(товар=item, количество=quantity, цена=price, покупатель=buyer, дата=date)
    with open('orders.json', 'w') as outfile:

        json.dump(data, outfile,ensure_ascii = False,indent=4)

if __name__ == "__main__":
    write_order_to_json('телефон', 2, 18000, 'Сергей', '10.12.2018')

# 3. найти любую книгу fb2 и определить какой там формат и написать свой генератор книжек на питоне, который будет
# принимать текст и какую-нибудь служебную инфу типа название книги, автор, издание и тд, и создавать файл в формате .fb2
# Проверить на любой читалке


def FictionBook(data):
    FictionBook = f'<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">{data}</FictionBook>'
    return FictionBook


def author(data):
    author = f'<author>{data}</author>'
    return str(author)


def title(data):
    title = f'<title>{data}</title>'
    return title


def p(data):
    p = f'<p>{data}</p>'
    return p


def compiling_text(author, title, p):
    text = f'{author}{title}{p}'
    return str(text)


def write_to_file(data):
    f = open('book.fb2', 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>')
    f.write(data)
    f.close()


author_text = author(input('имя автора:'))
title_text = title(input('заголовок:'))
p_text = p(input('текст:'))
text = FictionBook(compiling_text(author_text, title_text, p_text))
write_to_file(text)

# 4. Написать программу, которая принимает определенные настройки через JSON файл. Например прога для аутентификации
# пользователя.
# Мы при запуске загружаем JSON файл конфиг, в котором есть имя пользователя и пароль. А в процессе спрашиваем
# логин\пароль и если они совпали, то говорим что всё хорошо, иначе говорим, что мы вас не знаем

import json
import os


def authorized_keys():
    filename = os.path.join(os.path.dirname(__file__), 'authorized_keys.json')
    with open(filename, 'r') as f:
        data = json.loads(f.read())
    return data


def start(data):
    while True:
        login = input('Введите логин:')
        if login == data.get("login"):
            password = input('Введите пароль:')
            if password == data.get("password"):
                print('Добро пожаловать в систему')
                break
            else:
                print('Неверный пароль')
        else:
            print('Пользователь не найден')


if __name__ == "__main__":
    start(authorized_keys())
