import pymorphy3
import pymorphy3_dicts_ru
from translate import Translator
import csv

def words():
    f = open('messages.txt', mode="r", encoding="utf8")
    strings = f.read().splitlines()
    f.close()
    stringslist = [strings[i].split(' ') for i in range(len(strings))]
    clear_stringslist = []
    for i in range(len(stringslist)):
        for word in stringslist[i]:
            word = ''.join(filter(str.isalpha, word)).lower()
            if len(word) > 0:
                clear_stringslist.append(word)
    return clear_stringslist

def normwords(clear_stringslist):
    normallist = []
    for word in clear_stringslist:
        morph = pymorphy3.MorphAnalyzer()
        normallist.append(morph.parse(word)[0].normal_form)
    return normallist

def cntwords(normallist):
    d = {}
    for i in range(len(normallist)):
        if not normallist[i] in d:
            d[normallist[i]] = 1
        else:
            d[normallist[i]] += 1
    return d

def sortwords(d):
    sorted_d = sorted(d.items(), key=lambda n: n[1])
    sorted_d.reverse()
    return sorted_d

def translatedwords(sorted_list):
    translated_dictionary = []
    for i in range(len(sorted_list)):
        translation = Translator(from_lang='ru', to_lang="en").translate(str(sorted_list[i][0]))
        translated_dictionary.append([sorted_list[i][0], translation, sorted_list[i][1]])
        print(f'Переведено {i}/{len(sorted_list)} слов')
    return translated_dictionary