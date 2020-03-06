import datetime as dt
from marshmallow import Schema, fields


# https://marshmallow.readthedocs.io/en/stable/quickstart.html
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)

# Create a schema by defining a class with variables mapping attribute names to Field objects.
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

# create a schema from a dictionary of fields using the from_dict method.
UserSchemaA = Schema.from_dict(
    {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
)
