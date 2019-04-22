from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    q:普通关键字 isbn
    page:
    :return:
    '''
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成，含有一些'-'
    isbn_or_key = is_isbn_or_key(q)

    pass


def helloo():
    return 'hello,smart Eric!'

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
