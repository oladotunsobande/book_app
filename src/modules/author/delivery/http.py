from flask import Blueprint, request
from kanpai import Kanpai

from src.utils.responses import set_response
from src.utils.exceptions import ValidationError
import src.modules.author.service as authorService

def print_error(err):
  print('Error: ',err)

def create_author(payload):
  try:
    schema = Kanpai.Object({
      'first_name': Kanpai.String(error="'first_name' must be a string")
        .trim()
        .required(error="'first_name' is required"),
      'last_name': Kanpai.String(error="'last_name' must be a string")
        .trim()
        .required(error="'last_name' is required")
    })

    validation = schema.validate(payload)
    if validation.get('error') != None:
      error = list(validation.get('error').values())[0]
      raise ValidationError(error)

    return authorService.create_author(payload)
  except ValidationError as err:
    print_error(err)

    return set_response(
      status = 'BAD_REQUEST', 
      success = False,
      error = str(err)
    )
  except Exception as err:
    print_error(err)

    return set_response(
      status = 'SERVER_ERROR', 
      success = False,
      error = 'An error occurred'
    )    

def get_author(author_id):
  try:
    schema = Kanpai.Object({
      'author_id': Kanpai.Number(error="'author_id' must be a number")
        .required(error="'author_id' is required")
    })

    validation = schema.validate({ "author_id": author_id })
    if validation.get('error') != None:
      error = list(validation.get('error').values())[0]
      raise ValidationError(error)

    return authorService.get_author(author_id)
  except ValidationError as err:
    print_error(err)

    return set_response(
      status = 'BAD_REQUEST', 
      success = False,
      error = str(err)
    )
  except Exception as err:
    print_error(err)

    return set_response(
      status = 'SERVER_ERROR', 
      success = False,
      error = 'An error occurred'
    )