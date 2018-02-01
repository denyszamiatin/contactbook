def contact_exists(message, func=lambda x: x):
    def decorator(f):
        def wrapper(self, name, *args):
            if func(self.is_exist(name)):
                return f(self, name, *args)
            else:
                raise KeyError(message)

        return wrapper

    return decorator


class PhoneBook(object):
    def __init__(self):
        self.phonebook = {}

    def is_exist(self, name):
        return name in self.phonebook

    @contact_exists('Contact already exists', lambda x: not x)
    def create(self, name, phone):
        self.phonebook[name] = phone

    @contact_exists("Contact doesn't exist")
    def read(self, name):
        return self.phonebook[name]

    @contact_exists("Contact doesn't exist")
    def update(self, name, phone):
        self.phonebook[name] = phone


    @contact_exists("Contact doesn't exist")
    def delete(self, name):
        del self.phonebook[name]

phonebook = PhoneBook()

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