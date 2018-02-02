def contact_exists(message, func=lambda x: x):
    def decorator(f):
        def wrapper(self, name, *args):
            if func(self.is_exist(name)):
                return f(self, name, *args)
            else:
                raise KeyError(message)

        return wrapper

    return decorator


def autosave(f):
    def wrapper(self, *args):
        res = f(self, *args)
        self.serializer.save(self.phonebook)
        return res
    return wrapper


class PhoneBook(object):
    def __init__(self, serializer):
        self.serializer = serializer
        try:
            self.phonebook = serializer.load()
        except IOError:
            self.phonebook = {}

    def is_exist(self, name):
        return name in self.phonebook

    def list_all(self):
        return self.phonebook.items()

    @autosave
    @contact_exists('Contact already exists', lambda x: not x)
    def create(self, name, phone):
        self.phonebook[name] = phone

    @contact_exists("Contact doesn't exist")
    def read(self, name):
        return self.phonebook[name]

    @autosave
    @contact_exists("Contact doesn't exist")
    def update(self, name, phone):
        self.phonebook[name] = phone

    @autosave
    @contact_exists("Contact doesn't exist")
    def delete(self, name):
        del self.phonebook[name]
