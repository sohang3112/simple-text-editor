from flask import Flask, render_template, request, redirect
from pathlib import Path
import logging
import sys

class FormRequest:
    def __init__(self):
        self._attributes = {}
    
    def __getattr__(self, attr):
        try:
            return self._attributes[attr]
        except KeyError:
            ans = self._attributes[attr] = request.form.get(attr)
            return ans

app = Flask(__name__)

def user_file_path(name):
    return Path('user-files', name).with_suffix('.txt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/open_file/<name>')
def open_file(name):
    app.logger.info(f'Opening file {name}')
    return user_file_path(name).read_text()

@app.route('/save_file', methods=['POST'])
def save_file():
    req = FormRequest()
    app.logger.info(f'Saving file {req.name}')
    user_file_path(req.name).write_text(req.content)
    return redirect('/')

if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True)
