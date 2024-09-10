#!/usr/bin/env python3
'''i18n internationalization'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Defining defaults'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''get locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def display() -> str:
    '''Flask set up'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
