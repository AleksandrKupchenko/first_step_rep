import turtle
from flask import(
    Flask,
    render_template,
    request,

)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html',)

@app.route('/log')
def log():
    return render_template('login.html',)

@app.route('/about')
def about():
    return render_template('about.html',)

if __name__ == '__main__':
    app.run(debug=True)

    # Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

# Устанавливаем цвет черепашки
t.color("red")

# Рисуем квадрат
for _ in range(4):
    t.forward(100)  # Двигаемся вперед на 100 единиц
    t.left(90)      # Поворачиваем на 90 градусов

# Закрыть окно по клику
screen.exitonclick()