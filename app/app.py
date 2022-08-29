from flask import Flask, render_template, request, redirect, url_for
import flask


app = Flask(__name__)

records = ['Первая запись', 'Вторая запись', 'Третья запись']

# Получить все записи
def get_all_records():
    return records

# Удалить запись по id
def delete_record(id):
    records.pop(id-1)


# Создать запись
def create_record(text):
    records.append(text)


@app.route('/')
def index():
    records = get_all_records()
    return render_template('index.html', records=records)


@app.route('/create_record', methods=['POST'])
def create():
    if request.method == 'POST':
        text = request.form.get('text')
        create_record(text)
        return redirect(url_for('index'))
    return flask.abort(404)


@app.route('/delete_record/<int:id>')
def delete(id):
    if request.method == 'GET':
        delete_record(id)
        return redirect(url_for('index'))
    return flask.abort(404)
