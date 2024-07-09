from flask import Flask, request
from os import getenv
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import db
from routes import router
from flask_babel import Babel
from datetime import datetime

load_dotenv(override=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BABEL_DEFAULT_LOCALE"] = "en"
app.config["BABEL_SUPPORTED_LOCALES"] = ["en", "tr", "es"]
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "../translations"

db.init_app(app)
migrate = Migrate(app, db)


def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


babel = Babel(app, locale_selector=get_locale)

app.register_blueprint(router)


@app.context_processor
def utility_processor():
    return {
        "lang": get_locale(),
        "current_year": datetime.now().year,
        "copyright_url": getenv("COPYRIGHT_URL")
    }


if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
