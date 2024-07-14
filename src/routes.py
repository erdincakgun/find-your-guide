from flask import Blueprint, render_template
from flask_babel import _

router = Blueprint('router', __name__)


@router.route("/<lang>/")
def index(lang):
    context = {}
    context.update({
        "title": _("Find Your Guide | Home Page")
    })
    return render_template("index.html", **context)

@router.route("/<lang>/about")
def about(lang):
    context = {}
    context.update({
        "title": _("Find Your Guide | About")
    })
    return render_template("about.html", **context)

@router.route("/<lang>/contact")
def contact(lang):
    context = {}
    context.update({
        "title": _("Find Your Guide | Contact")
    })
    return render_template("contact.html", **context)

@router.route("/<lang>/guides")
def guides(lang):
    context = {}
    context.update({
        "title": _("Find Your Guide | Guides")
    })
    return render_template("guides.html", **context)