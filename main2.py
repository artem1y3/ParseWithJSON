import requests
import sqlite3


def get_json(url):
    r = requests.get(url)
    return r.json()


def write_to_file(dicts):
    with open("info.txt", "a") as f:
        f.write("===============================================\n")
        for d, j in dicts.items():
            f.write(d + ": " + j + "\n")
        f.write("===============================================\n")


def write_to_db(dict,base):
    base.execute("""
        INSERT INTO zakupki
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """,(
            dict["number"],
            dict["fz"],
            dict["url"],
            dict["dateZakupkaStart"],
            dict["dateZakupkaEnd"],
            dict["zajavkaPrice"],
            dict["zajavkaHavePrice"],
            dict["contractPrice"],
            dict["companyName"],
            dict["companyInn"],
            dict["companyPlace"]
        )
    )


def show_to_console(dicts):
    print("===============================================")
    for o, j in dicts.items():
        print(str(o) + ": " + str(j))
    print("===============================================")


def main():
    conn = sqlite3.connect("my_base.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    # cursor.execute("""
    #   CREATE TABLE zakupki(
    #     number INTEGER,
    #     fz INTEGER,
    #     url VARCHAR(200),
    #     dateZakupkaStart VARCHAR(50),
    #     dateZakupkaEnd VARCHAR(50),
    #     zajavkaPrice INTEGER,
    #     zajavkaHavePrice INTEGER,
    #     contractPrice INTEGER,
    #     companyName VARCHAR(400),
    #     companyInn INTEGER,
    #     companyPlace VARCHAR(200)
    #   )
    # """)
    # print(cursor.fetchall())




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
            write_to_db(js,cursor)
            dicts = {}
            conn.commit()

    if input("Отобразить закупки из базы данных? (да/нет): ") == "да":
        for row in cursor.execute("SELECT * FROM zakupki;"):
            print(row)

if __name__ == '__main__':
    main()
