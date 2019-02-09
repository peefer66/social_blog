from flask import Flask

#Create an instance of Flask
app = Flask(__name__)

# Register Blueprints
from companyblog.core.views import core
app.register_blueprint(core)

