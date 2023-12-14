from english_learn import *


def show():
    list = words()
    print(list)
    normal_list = (normwords(list))
    print(normal_list)
    d = cntwords(normal_list)
    print(d)
    sorted_list = (sortwords(d))
    print(sorted_list)
    dictionary = translatedwords(sorted_list)
    with open('dictionary.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Cлово', 'Перевод', 'Количество повторений'])
        for i in dictionary:
            writer.writerow(i)
    print('Словарь создан!')


if __name__ == "__main__":
    show()