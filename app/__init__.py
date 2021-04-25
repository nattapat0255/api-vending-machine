from flask import Flask
from flask_cors import CORS
import os

from .instance.config import DevConfig, ProdConfig
from .api.routes import api

def create_app():
  app = Flask(__name__)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  app.register_blueprint(api)
  env = os.environ.get('FLASK_ENV','production')
  if env == 'development':
    app.config.from_object(DevConfig)
  else:
    app.config.from_object(ProdConfig)
  return app