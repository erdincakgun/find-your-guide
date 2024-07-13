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

@router.route("/about")
def about():
    context = {}
    context.update({
        "title": _("Find Your Guide | About")
    })
    return render_template("about.html", **context)

@router.route("/contact")
def contact():
    context = {}
    context.update({
        "title": _("Find Your Guide | Contact")
    })
    return render_template("contact.html", **context)

@router.route("/guides")
def guides():
    context = {}
    context.update({
        "title": _("Find Your Guide | Guides")
    })
    return render_template("guides.html", **context)