from flask import jsonify, Blueprint,request
from app.forms.book import SearchForm

from helper import is_isbn_or_key
from yushu_book import YuShuBook

# 蓝图blueprint
web = Blueprint('web', __name__)

@web.route('/book/search')
def search():
    '''
    q:普通关键字 isbn
    page:
    '''
    # q至少有一个字符，长度限制
    form = SearchForm(request.args)
    if form.validate():
        q = form.page.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify({'msg':'参数校验失败'})