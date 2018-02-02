from xml.etree import ElementTree as ET
import re

import serializer


phone_pattern = re.compile(r'\d{3}-\d{2}-\d{2}')


config = ET.parse('settings.xml')
serializer_name = config.find('.//serializer').text.strip()
if serializer_name == 'JSON':
    import model
    phonebook = model.PhoneBook(serializer.JsonSerializer())
elif serializer_name == 'CSV':
    import model
    phonebook = model.PhoneBook(serializer.CsvSerializer())
elif serializer_name == 'DB':
    import db_model
    phonebook = db_model.PhoneBook()
else:
    raise NameError("Incorrect settings")


def input_phone():
    while True:
        phone = raw_input('Phone?')
        if phone_pattern.match(phone):
            return phone


def create_contact():
    name = raw_input('Name?')
    phone = input_phone()
    phonebook.create(name, phone)


def read_contact():
    name = raw_input('Name?')
    print phonebook.read(name)


def update_contact():
    name = raw_input('Name?')
    phone = input_phone()
    phonebook.update(name, phone)


def delete_contact():
    name = raw_input('Name?')
    phonebook.delete(name)


def dummy():
    print "Incorrect action"


ACTIONS = {
    'c': create_contact,
    'r': read_contact,
    'u': update_contact,
    'd': delete_contact,
}

while True:
    action = raw_input('''Actions:
c - create
r - read
u - update
d - delete
q - quit ''').lower()
    try:
        if action == 'q':
            break
        ACTIONS.get(action, dummy)()
    except KeyError as e:
        print e