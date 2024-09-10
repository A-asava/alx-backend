#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Supported languages configuration
app.config['LANGUAGES'] = ['en', 'fr']

# user databas
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Babel initialization
babel = Babel(app)

@babel.localeselector
def get_locale():
    #Local from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    #Locale from logged-in user's settings
    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user["locale"]

    #Locale from request header (Accept-Language)
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """ Get user by ID from URL parameter `login_as` """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users.get(int(user_id))
        except ValueError:
            return None
    return None

@app.before_request
def before_request():
    """ Retrieve user and store it in flask.g """
    g.user = get_user()

@app.route('/')
def index():
    return render_template('6-index.html')

if __name__ == "__main__":
    app.run(debug=True)

