from app.libs.httper import HTTP
from flask import current_app

class YuShuBook:
    # 模型层 MVC  M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls,keyword,page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.get_start_page(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def get_start_page(page):
        return (page-1) * current_app.config['PER_PAGE']