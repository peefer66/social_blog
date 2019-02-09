from flask import Flask

#Create an instance of Flask
app = Flask(__name__)

# Register Blueprints
from companyblog.core.views import core
from companyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)

