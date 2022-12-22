from pprint import pprint
import csv
import re


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def phonebook(contacts_list):
    my_list = []
    for i in contacts_list:
        full_name = ' '.join(i[:3]).split(' ')
        if 'доб' not in i[5]:
            pattern = r'(\+7|8)\s*\(*(495)\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*'
            result = re.sub(pattern, r'+7(\2)\3-\4-\5', i[5])
            my_list.append([full_name[0], full_name[1],
                        full_name[2], i[3], i[4], result, i[6]])
        else:
            pattern = r'(\+7|8)\s*\(*(495)\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(*(\w*[.])\s(\d{4})\)*'
            result = re.sub(pattern, r'+7(\2)\3-\4-\5 \6\7', i[5])
            my_list.append([full_name[0], full_name[1],
                        full_name[2], i[3], i[4], result, i[6]])
    return contact_info(my_list)


def contact_info(contacts):
    for contact in contacts:
        name = contact[1]
        last_name = contact[0]
        for el_contact in contacts:
            el_name = el_contact[1]
            el_last_name = el_contact[0]
            if name == el_name and last_name == el_last_name:
                if contact[2] == "":
                    contact[2] = el_contact[2]
                if contact[3] == "":
                    contact[3] = el_contact[3]
                if contact[4] == "":
                    contact[4] = el_contact[4]
                if contact[5] == "":
                    contact[5] = el_contact[5]
                if contact[6] == "":
                    contact[6] = el_contact[6]

    result_list = []
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(
        f, delimiter=',')
    datawriter.writerows(phonebook(contacts_list))
