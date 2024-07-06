from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    app.run("0.0.0.0", 80, debug=True)
