from flask import Blueprint, render_template
from flask_babel import _

router = Blueprint('router', __name__)


@router.route("/")
def index():
    context = {}
    context.update({
        "title": _("Find Your Guide | Home Page")
    })
    return render_template("index.html", **context)
