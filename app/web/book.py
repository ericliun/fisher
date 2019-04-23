from flask import jsonify, request
from app.forms.book import SearchForm
from . import web

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    '''
    q:普通关键字 isbn
    page:
    '''
    # q至少有一个字符，长度限制
    form = SearchForm(request.args)
    if form.validate():
        q = str(form.q.data).strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)