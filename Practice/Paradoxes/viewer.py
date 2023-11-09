from montyhall import *
from birthdayparadox import *


def show():
    print('Выберите парадокс:')
    print('1. Парадокс Монти Холла')
    print('2. Парадокс Дней рождения')
    c = input()
    if c=='1':
        p=input('Введите количество раз:')
        if p=='':
            print(f'Процент побед в двух случаях: {monty_hall(1000)}')
        elif p.isdigit():
            print(f'Процент побед в двух случаях: {monty_hall(int(p))}')
        else:
            print('Ошибка!\n')
            show()
    elif c=='2':
        p1=input("Введите количество раз:")
        p2=input("Введите количество человек в группе:")
        ent=print('\n')
        if p1=='' and p2=='':
            print(f'Процент совпадений дня рождения при 23: {birthday(1000, 23)}')
            print(f'Процент совпадений дня рождения при 60: {birthday(1000, 60)}')
        elif p1.isdigit() and p2.isdigit():
            print(f'Процент совпадений дней рождения:{birthday(int(p1), int(p2))}')
        else:
            print('Ошибка!\n')
            show()
    else:
        show()
if __name__ == "__main__":
    show()
while True:
