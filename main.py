from pprint import pprint
import csv
import re


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

my_list = []
for i in contacts_list:
    lastname = str(i).split()[0].split('\'')[1]
    name = str(i).split()[1].split(",")[0].replace("'","")
    middlename = str(i).split()[2].split(",")[0].replace("'","")
    org = str(i).split(',')[3].strip(" \'")
    position = str(i).split(',')[4].strip(" \' ")
    tel = str(i).split(',')[5].strip(" \' ")
    email = str(i).split(',')[6].strip(" \' ]")
    if 'доб' not in tel:
        pattern = r'(\+7|8)\s*\(*(495)\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*'
        result = re.sub(pattern, r'+7(\2)\3-\4-\5', tel)
        string = [f'{lastname} {name} {middlename} {org} {position} {result} {email}']
        my_list.append(string)
    else:
        pattern = r'(\+7|8)\s*\(*(495)\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(*(\w*[.])\s(\d{4})\)*'
        result = re.sub(pattern, r'+7(\2)\3-\4-\5 \6\7', tel)
        string = [f'{lastname} {name} {middlename} {org} {position} {result} {email}']
        my_list.append(string)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(my_list)
