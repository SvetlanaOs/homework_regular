from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for i in range (1,len(contacts_list)):
  fio = contacts_list[i][0] + ' '+ contacts_list[i][1] + ' ' + contacts_list[i][2]
  fio_list = fio.split()
  for j in range (len(fio_list)):
    contacts_list[i][j] = fio_list[j]
  if contacts_list[i][5] != '':
    pattern = r"(\+7|8)?\s*?\(?(\d{3})\)?\-?\s*(\d{3})[\s-]*(\d{2})[\s-]*(\d+)\s*\(?(доб.)?\s*?(\d+)?\)?"
    pattern_sub = r"+7(\2)\3-\4-\5 \6\7"
    contacts_list[i][5] = re.sub(pattern, pattern_sub, contacts_list[i][5])

contacts_dict = {}
header = contacts_list[0]

for contact in contacts_list[1:]:
  lastname = contact[0]
  firstname = contact[1]
  surname = contact[2]
  organization = contact[3]
  position = contact[4]
  phone = contact[5]
  email = contact[6]

  key = (lastname, firstname)

  if key not in contacts_dict:
    contacts_dict[key] = [lastname, firstname, surname, organization, position, phone, email]
  else:
    existing_contact = contacts_dict[key]
    for i, value in enumerate([surname, organization, position, phone, email]):
      if value and not existing_contact[i + 2]:
        existing_contact[i + 2] = value

contacts_list = [header] + list(contacts_dict.values())

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
