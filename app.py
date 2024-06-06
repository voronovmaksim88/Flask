from flask import Flask, render_template

# Создаем экземпляр Flask
app = Flask(__name__)


# Определяем маршрут для главной страницы
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return "<h1> О сайте </h1>"


# Запускаем сервер, если этот файл выполнен как главный
if __name__ == '__main__':
    app.run(debug=True)
