from flask import Flask, render_template, request, redirect
import model
import serializer

app = Flask(__name__)
phonebook = model.PhoneBook(serializer.JsonSerializer())

@app.route('/')
def index():
    contacts = phonebook.list_all()
    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = phone = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        if name and phone:
            phonebook.create(name, phone)
            return redirect('/')
    return render_template('add.html', name=name, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)