import os

from flask import Flask
from flaskr.api.healthycheck import healthy_check_bp

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
  )

  app.register_blueprint(healthy_check_bp)

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)
  
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  return app