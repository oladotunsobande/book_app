from flask import Blueprint, request
from kanpai import Kanpai

from src.utils.responses import set_response
from src.utils.exceptions import ValidationError
import src.modules.author.service as authorService

author_routes = Blueprint("author_routes", __name__)

# Create new author
@author_routes.route('/', methods=['POST'])
def create_author():
  try:
    payload = request.get_json()

    schema = Kanpai.Object({
      'first_name': Kanpai.String()
        .trim()
        .required(),
      'last_name': Kanpai.String()
        .trim()
        .required()
    })

    validation = schema.validate(payload)
    if validation.get('error') != None and type(validation.get('error')) == str:
      raise ValidationError('BAD_REQUEST', validation.get('error'))

    return authorService.create_author(payload)
  except ValidationError as args:
    print(args['error'])

    return set_response(
      status = args['status'], 
      success = False,
      error = args['error']
    )
  except Exception:
    return set_response(
      status = 'SERVER_ERROR', 
      success = False,
      error = 'An error occurred'
    )    