from sqlalchemy import and_

class Repository:
  def __init__(self, entity, schema):
    self.entity = entity
    self.schema = schema

  def get_one(self, id):
    record = self.entity.query.get(id)

    if(record != None):
      return Repository.dump_record(self.schema, record)
    else:
      return record

  def get_one_by(self, fields):
    filters = Repository.set_filters(self.entity, fields)
    record = self.entity.query.filter(filters)

    if(record != None):
      return Repository.dump_record(self.schema, record)
    else:
      return record

  def get_all(self, skip=0, limit=20):
    records = self.entity.query.all().offset(skip).limit(limit)
    return Repository.dump_record(self.schema, records)

  def get_all_by(self, fields, skip=0, limit=20):
    filters = Repository.set_filters(self.entity, fields)
    records = self.entity.query.filter(filters).all().offset(skip).limit(limit)

    return Repository.dump_record(self.schema, records)

  def persist(self, payload):
    table_row = self.entity(**payload)
    new_record = table_row.create()

    return Repository.dump_record(self.schema, new_record)

  @staticmethod
  def dump_record(schema, record):
    return schema.dump(record)

  @staticmethod
  def set_filters(table, list):
    filters = []

    for key, value in list.items():
      filters.append(getattr(table,key) == value)

    return and_(**filters)
