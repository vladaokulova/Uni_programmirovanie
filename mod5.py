from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    try:
        nums = [int(num) for num in numbers.split('/')]
        max_num = max(nums)
        return f'Максимальное число: <i>{max_num}</i>'
    except ValueError:
        return 'Переданы некорректные данные'

if __name__ == "__main__":
    app.run(debug=True)
