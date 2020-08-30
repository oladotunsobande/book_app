from src.config.db import db
from src.utils.responses import set_response
from src.modules.author.model.author import Author, AuthorSchema

def create_author(payload):
  try:
    author_schema = AuthorSchema()

    author, error = author_schema.loads(payload)
    result = author_schema.dumps(author.create()).data

    return set_response(
      status = 200, 
      value = { 
        "success": True,
        "message": "New author created successfully",
        "data": result 
      }
    )
  except Exception as error:
    raise error
