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
    print(error)
    raise error

def get_all_authors(skip, limit):
  try:
    temp_skip = int(skip)
    temp_limit = int(limit)

    authors = Author.query.all().limit(temp_limit).offset(temp_skip)
    author_schema = AuthorSchema(many=True)

    result = author_schema.dump(authors)

    return set_response(
      status = 'SUCCESS',
      success = True,
      data = result
    )
  except Exception as error:
    print(error)
    raise error

def get_author(authorId):
  try:
    author = Author.query.get(authorId)
    author_schema = AuthorSchema()

    result = author_schema.dump(author)

    return set_response(
      status = 'SUCCESS',
      success = True,
      data = result
    )
  except Exception as error:
    print(error)
    raise error