from flask import Flask
from os import getenv
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import db
from routes import router

load_dotenv(override=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(router)

if __name__ == "__main__":
    app.run("0.0.0.0", 80, debug=True)
