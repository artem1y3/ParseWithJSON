import requests
from bs4 import BeautifulSoup
import csv
import zipfile
import os


def get_json(url):
    r = requests.get(url)
    return r.json()


def write_to_file(dicts):
    with open("info.txt", "a") as f:
        f.write("===============================================\n")
        for d, j in dicts.items():
            f.write(d + ": " + j + "\n")
        f.write("===============================================\n")


def write_to_db():
    pass


def show_to_console(dicts):
    print("===============================================")
    for o, j in dicts.items():
        print(str(o) + ": " + str(j))
    print("===============================================")


def main():
    atr = {
        'number': "Номер",
        'fz': "ФЗ",
        'url': "Ссылка",
        'dateZakupkaStart': "Дата начала",
        'dateZakupkaEnd': "Дата окончания",
        'zajavkaPrice': "Цена заявки",
        'zajavkaHavePrice': "Имеющаяся цена",
        'contractPrice': "Цена по контракту",
        'companyName': "Название компании",
        'companyInn': "ИНН компании",
        'companyPlace': "Местоположение компании",
        'lots': "Лоты",
        'zakupkaObject': "Объект закупки"
    }
    url = 'http://phpnt.com/zakupki/get?regNumber='
    file = 'info.txt'
    dicts = {}
    while True:
        s = input("Введите номер закупки: ")
        if s == "exit":
            break
        else:
            js = get_json(url + s)
            for o, j in js.items():
                dicts[str(atr[o])] = str(j)
            show_to_console(dicts)
            write_to_file(dicts)
            dicts = {}


if __name__ == '__main__':
    main()
