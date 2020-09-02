class ValidationError(Exception):

  def __init__(self, status, error):
    self.status = status
    self.error = error

  def __str__(self):
    return {
      'status': self.status,
      'error': self.error
    }