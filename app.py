from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return 'hey'


@app.route('/<name>')
def index_name(name):
    return 'hey {}, how are you?'.format(name)

if __name__ == '__main__':
    app.run()
