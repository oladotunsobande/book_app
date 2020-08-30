from flask import make_response, jsonify

def set_response(status, value = None):  
  return make_response(jsonify(value), status)