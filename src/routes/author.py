from flask import Blueprint, request

import src.modules.author.service as authorService

author_routes = Blueprint("author_routes", __name__)

# Create new author
@author_routes.route('/', methods=['POST'])
def create_author():
  try:
    payload = request.get_json()
    return authorService.create_author(payload)
  except Exception as error:
    raise error