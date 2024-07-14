from flask import redirect
from flask import Flask, request, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import getenv
from dotenv import load_dotenv
from flask_migrate import Migrate
from src.models import db, Guide, Event, User
from src.routes import router, mail
from flask_babel import Babel
from datetime import datetime
from flask_login import LoginManager
from flask_login import current_user


load_dotenv(override=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BABEL_DEFAULT_LOCALE"] = "en"
app.config["BABEL_SUPPORTED_LOCALES"] = ["en", "tr", "es"]
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "../translations"
app.config['MAIL_SERVER'] = getenv("SMTP_HOST")
app.config['MAIL_PORT'] = getenv("SMTP_PORT")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = getenv("SMTP_USER")
app.config['MAIL_PASSWORD'] = getenv("SMTP_PASS")
app.config['MAIL_DEFAULT_SENDER'] = getenv("SMTP_USER")
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

mail.init_app(app)
db.init_app(app)

migrate = Migrate(app, db)


admin = Admin(app, name='Find Your Guide | Admin Panel',
              template_mode='bootstrap3')


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('router.login'))


admin.add_view(AdminModelView(Guide, db.session))
admin.add_view(AdminModelView(Event, db.session))

login_manager = LoginManager()
login_manager.login_view = 'router.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def get_locale():
    try:
        path_locale = request.path.split('/')[1]
        if path_locale in app.config['BABEL_SUPPORTED_LOCALES']:
            return path_locale
    except IndexError:
        pass
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


babel = Babel(app, locale_selector=get_locale)

app.register_blueprint(router)


@app.route('/')
def redirect_to_default_language():
    return redirect(url_for('router.index', lang=app.config['BABEL_DEFAULT_LOCALE']))


@app.context_processor
def utility_processor():
    return {
        "lang": get_locale(),
        "current_year": datetime.now().year,
        "copyright_url": getenv("COPYRIGHT_URL"),
        "whatsapp_number": getenv("WHATSAPP_NUMBER"),
    }


if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
