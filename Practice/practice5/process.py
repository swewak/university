import os
def process():
    try:
        name = input('Введите название файла, из которого хотите импортировать данные: ').strip()
        f = open(name)
        n = int(f.readline())
        a = [int(x) for x in f.readlines()]
        f.close()
        return a
    except FileNotFoundError:
        print("Такого файла нет! Введите название ещё раз! ")
        return process()
    except NotADirectoryError:
        print()