from flask import Flask

app = Flask(__name__)

storage = {}


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    year = int(date[:4])
    month = int(date[4:6])

    storage.setdefault(year, {}).setdefault(month, 0)
    storage[year][month] += number

    return f'Трата {number} руб. добавлена за {date}'


@app.route('/calculate/<int:year>')
def calculate_year(year):
    total = sum(storage.get(year, {}).values())
    return f'Сумма трат за {year} год: {total} руб.'


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    total = storage.get(year, {}).get(month, 0)
    return f'Сумма трат за {month} месяц {year} года: {total} руб.'


if __name__ == "__main__":
    app.run(debug=True)
