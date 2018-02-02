from xml.etree import ElementTree as ET

import model
import serializer

config = ET.parse('settings.xml')
serializer_name = config.find('.//serializer').text.strip()
if serializer_name == 'JSON':
    phonebook = model.PhoneBook(serializer.JsonSerializer())
elif serializer_name == 'CSV':
    phonebook = model.PhoneBook(serializer.CsvSerializer())
else:
    raise NameError("Incorrect settings")


def create_contact():
    name = raw_input('Name?')
    phone = raw_input('Phone?')
    phonebook.create(name, phone)


def read_contact():
    name = raw_input('Name?')
    print phonebook.read(name)


def update_contact():
    name = raw_input('Name?')
    phone = raw_input('Phone?')
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