from flask import Flask

# Создаем экземпляр Flask
app = Flask(__name__)


# Определяем маршрут для главной страницы
@app.route('/')
def home():
    return "Hello, World!"


# Запускаем сервер, если этот файл выполнен как главный
if __name__ == '__main__':
    app.run(debug=True)
