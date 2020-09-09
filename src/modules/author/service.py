from src.config.db import db
from src.utils.responses import set_response
from src.modules.repository import Repository
from src.modules.author.model.author import Author, AuthorSchema

def create_author(payload):
  try:
    author_repository = Repository(Author, AuthorSchema())
    result = author_repository.persist(payload)

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

def get_author(author_id):
  try:
    author_repository = Repository(Author, AuthorSchema())
    result = author_repository.get_one(author_id)

    if(result == None):
      return set_response(
        status = 'NOT_FOUND',
        success = False,
        error = 'Author record does not exist'
      )

    return set_response(
      status = 'SUCCESS',
      success = True,
      data = result
    )
  except Exception as error:
    print(error)
    raise error