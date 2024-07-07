from flask import Blueprint, render_template

router = Blueprint('router', __name__)


@router.route("/")
def index():
    context = {}
    context.update({"title": "Find Your Guide | Home Page"})
    return render_template("index.html", **context)
