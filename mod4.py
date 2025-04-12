from flask import Flask
from datetime import datetime

app = Flask(__name__)

WEEKDAYS = [
    'понедельника', 'вторника', 'среды',
    'четверга', 'пятницы', 'субботы', 'воскресенья'
]

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    return f'Привет, {name}. Хорошей {WEEKDAYS[weekday]}!'

if __name__ == "__main__":
    app.run(debug=True)
