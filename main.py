import logging
import sys
from flask import Flask, jsonify

from src.config.db import db
import settings as env
from src.utils.responses import set_response
from src.routes.author import author_routes

def create_app(config):
  app = Flask(__name__)

  app.config.from_object(config)

  db.init_app(app)
  
  with app.app_context():
    db.create_all()

  # Endpoint routes
  app.register_blueprint(author_routes, url_prefix='/v1/api/author')
  #app.register_blueprint(book_routes, url_prefix='/v1/api/books')

  @app.after_request
  def add_header(response):
    return response

  @app.errorhandler(500)
  def server_error(e):
    logging.error(e)
    return set_response(
      status = 500, 
      value = {
        "success": False,
        "error": "An error occurred"
      }
    )

  logging.basicConfig(
    stream = sys.stdout,
    format = '%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
    level = logging.DEBUG
  )

  return app