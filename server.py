from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Приложение готово'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 5000 - порт по умолчанию
    app.run(host='0.0.0.0', port=port)
