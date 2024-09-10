#!/usr/bin/env python3
'''i18n internationalization'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    '''Flask set up'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
