# TODO: Error Handling

from flask import Flask, render_template, request, redirect, abort

from functools import cache
from pathlib import Path
import logging
import sys


class FormRequest:
    """Easy access to form attributes in a POST method route"""
    
    @cache
    def __getattr__(self, attr: str) -> str:
        return request.form.get(attr)


def user_file_path(filename: str) -> Path:
    return Path('user-files', filename).with_suffix('.txt')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/open_file/<filename>')
def open_file(filename: str):
    app.logger.info(f'Opening file "{filename}"')
    try:
        return user_file_path(filename).read_text()
    except FileNotFoundError:
        app.logger.error(f'File "{filename}" not found')
        abort(404)

@app.route('/save_file', methods=['POST'])
def save_file():
    req = FormRequest()
    app.logger.info(f'Saving file {req.filename}')
    user_file_path(req.filename).write_text(req.content)
    return redirect('/')


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True)
