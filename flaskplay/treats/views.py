"""Views for treats product."""


from flask import render_template, request
from . import treats_blueprint


@treats_blueprint.route("/")
def index():
    return render_template("treats/th.html")


@treats_blueprint.route("/other")
def other():
    crash = request.args.get("crash")
    if crash:
        raise Exception("Foo")
    return render_template("treats/other.html")