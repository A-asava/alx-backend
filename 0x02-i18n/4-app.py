#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# List of supported languages
app.config['LANGUAGES'] = ['en', 'fr']

# Set default locale
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Check if 'locale' is in the request's arguments
    locale = request.args.get('locale')
    
    # If the locale is provided and in supported languages, return it
    if locale in app.config['LANGUAGES']:
        return locale
    
    # Otherwise, use the default
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(debug=True)

