from bas import *

def show():
    try:
        split_strings = (inf('info.csv'))
        name = input('Введите строку: ').strip()
        list = get_books(name, split_strings)
        out = (get_totals(list))
        if len(out) == 0:
            print('Таких книг нет')
        else:
            print(out)
    except:
        print('Ошибка')