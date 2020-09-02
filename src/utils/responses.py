from flask import make_response, jsonify

def set_response(status, success, data = None, message = None, error = None, token = None, count = None):  
  result = {}

  result['success'] = success

  if data is not None:
    result['data'] = data
  
  if message is not None:
    result['message'] = message

  if error is not None:
    result['error'] = error

  if token is not None:
    result['token'] = token

  if count is not None:
    result['count'] = count

  return make_response(jsonify(result), get_status_code(status))

def get_status_code(name):
  status_codes = {
    'SUCCESS': 200,
    'BAD_REQUEST': 400,
    'NOT_AUTHORIZED': 401,
    'NOT_FOUND': 404,
    'CONFLICT': 409,
    'SERVER_ERROR': 500    
  }

  return status_codes.get(name, 'Invalid status error')