import os
from flask import Flask
from api import api
from config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    return app


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(api)
app.app_context().push()

@app.route('/')
def index():
    return 'Hello World!'

app.run(port=5000)
