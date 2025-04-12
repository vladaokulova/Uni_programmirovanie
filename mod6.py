import os
from flask import Flask

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:file_path>')
def preview_file(size, file_path):
    try:
        abs_path = os.path.abspath(file_path)

        with open(abs_path, 'r') as file:
            content = file.read(size)

        return f'<b>{abs_path}</b> {len(content)}<br>{content}'

    except FileNotFoundError:
        return 'Файл не найден'
    except PermissionError:
        return 'Нет доступа к файлу'


if __name__ == "__main__":
    app.run(debug=True)
