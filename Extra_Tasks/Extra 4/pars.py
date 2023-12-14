import re
import csv
import urllib.request

adressrequest = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()
pattern = r"(?:class=\"org-widget-header__title-link\">)(?P<services>[^<]+)(?:[^0]+)(?:location\">[\s]+)(?P<street>[^<]+\b)(?:[^0-9]+)(?:value\">)(?P<number>[^<]+\b)(?:[^0-9,]+)(?:value\">)(?P<time>[^<]+)"
allmatches = re.findall(pattern, adressrequest)
with open('pars.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Сервис', 'Адрес', 'Контакт', 'Расписание'])
    for match in allmatches:
        match = list(match)
        filter_match = [match[j] for j in range(len(match)) if len(match[j].split()) != 0]
        writer.writerow(filter_match)