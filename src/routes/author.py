from flask import Blueprint, request

import src.modules.author.delivery.http as AuthorController

author_routes = Blueprint("author_routes", __name__)

# Create new author
@author_routes.route('/', methods=['POST'])
def create_author():
  return AuthorController.create_author(request.get_json())

# Get single author
@author_routes.route('/single/<int:author_id>', methods=['GET'])
def get_author(author_id):
  return AuthorController.get_author(author_id)
