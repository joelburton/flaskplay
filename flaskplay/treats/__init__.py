"""Treats product for Flask."""

from flask import Blueprint

treats_blueprint = Blueprint("treats",
                             __name__,
                             static_folder="static",
                             template_folder="templates",
                             )

# We need to import the views, so the decorators in that file get used -- however,
# we can't import that until we create the blueprint, or we'll have circular dependencies

from . import views
