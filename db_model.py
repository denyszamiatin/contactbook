import sqlite3

db = sqlite3.connect('phones.db')


class PhoneBook(object):
    def create(self, name, phone):
        cursor = db.cursor()
        cursor.execute(
            "insert into contacts (name, value) values (?, ?)",
            (name, phone)
        )
        cursor.close()
        db.commit()

    def read(self, name):
        cursor = db.cursor()
        contact = cursor.execute(
            'select name, phone from contacts where name=?',
            (name,)
        ).fetchone()
        cursor.close()
        return contact[1]

    def update(self, name, phone):
        cursor = db.cursor()
        cursor.execute(
            "update contacts set phone=? where name=?",
            (phone, name)
        )
        cursor.close()
        db.commit()

    def delete(self, name):
        cursor = db.cursor()
        cursor.execute(
            "delete from contacts where name=?",
            (name, )
        )
        cursor.close()
        db.commit()
