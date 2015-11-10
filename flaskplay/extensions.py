"""Extension configuration for my flask app.

These are done here so there's an easy import from blueprints and everywhere
else that needs these configurations. They should be initialized on the app itself
in the create_app function.
"""

from flask.ext import shelve

