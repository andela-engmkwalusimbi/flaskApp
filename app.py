from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hey'


@app.route('/<name>')
def index_name(name):
    return 'hey {}'.format(name)

if __name__ == '__main__':
	app.debug = True
    app.run()