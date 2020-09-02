from src.config.db import db
from src.utils.responses import set_response
from src.modules.author.model.author import Author, AuthorSchema

def create_author(payload):
  try:
    author = Author(first_name = payload['first_name'], last_name = payload['last_name'])
    author_schema = AuthorSchema()

    result = author_schema.dump(author.create())

    return set_response(
      status = 'SUCCESS', 
      success = True,
      data = result,
      message = 'New author created successfully'
    )
  except Exception as error:
    raise error
