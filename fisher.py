from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    # status code 200,404,301
    # content-type http headers
    # content-type = text/html
    # Response
    headers = {
        'content-type':'text/plain',
        'location':'http://www.bing.com'
    }
    # response= make_response('<html></html>', 301)
    # response.headers = headers
    return '<html></html>', 301, headers


def helloo():
    return 'hello,smart Eric!'

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
