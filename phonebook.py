phonebook = {}


def is_exist(name):
    return name in phonebook


def contact_exists(message, func=is_exist):
    def decorator(f):
        def wrapper(name, *args):
            if func(name):
                return f(name, *args)
            else:
                raise KeyError(message)
        return wrapper
    return decorator


@contact_exists('Contact already exists', lambda n: not is_exist(n))
def create(name, phone):
    phonebook[name] = phone


@contact_exists("Contact doesn't exist")
def read(name):
    return phonebook[name]


@contact_exists("Contact doesn't exist")
def update(name, phone):
    phonebook[name] = phone


@contact_exists("Contact doesn't exist")
def delete(name):
    del phonebook[name]


def create_contact():
    name = raw_input('Name?')
    phone = raw_input('Phone?')
    create(name, phone)


def read_contact():
    name = raw_input('Name?')
    print read(name)


def update_contact():
    name = raw_input('Name?')
    phone = raw_input('Phone?')
    update(name, phone)


def delete_contact():
    name = raw_input('Name?')
    delete(name)


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