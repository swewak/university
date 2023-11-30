import re

def flight():
    with open('flight.txt',encoding='utf8') as info:
        text=info.read().splitlines()
        text0=[]
        pattern=r'^Рейс\s\d+\s(прибыл\sиз|отправился\sв)\s\D+\s\в\s\S+$'

    for i in text:
        a=i.split()
        match=re.search(pattern,i)

        if match:
            text0.append(f'[{a[6]}] - Поезд № {a[1]} {a[3]} {a[4]}')

    with open('newflights.txt', mode='w',encoding='utf8') as words:
        for i in text0:
            words.write(f'{i}\n')
if __name__ == '__main__':
    flight()