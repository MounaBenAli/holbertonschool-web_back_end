#!/usr/bin/env python3
""" Get locale from request """
from flask import Flask, render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ configures available languages in the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Renders html template"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ returns the best match for the preferred lg from available languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
