from sqlalchemy import and_

class Repository:
  def __init__(self, entity, schema):
    self.entity = entity
    self.schema = schema

  def get_one(self, id):
    record = self.entity.query.get(id)
    return self.dump_record(record)

  def get_one_by(self, fields):
    helper = RepositoryHelper(self.entity)
    query = helper.set_filters(fields)

    record = self.entity.query.filter(query)
    return self.dump_record(record)

  def persist(self, payload):
    entity = self.entity(**payload)

    return self.dump_record(entity.create())

  def dump_record(self, record):
    return self.schema.dump(record)

# Schema repository helper class
class RepositoryHelper:
  def __init__(self, table):
    self.table = table

  def set_filters(self, list):
    filters = []

    for key, value in list.items():
      filters.append(getattr(self.table,key) == value)

    return and_(**filters)
