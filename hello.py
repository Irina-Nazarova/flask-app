# -*- coding: utf-8 -*-

"""
Импортируется класс Flask из пакета flask и создаётся экземпляр этого класса.
С помощью магического метода __name__ в конструктор этого класса передаётся имя файла hello.py.
Таким образом, теперь экземпляр app — это наше приложение.
На app навешивается декоратор @app.route, он связывает URL главной страницы '/' с функцией hello_world(),
точно как path() в Джанго. А функция hello_world() возвращает строку «Im do it!».
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Im do it!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
