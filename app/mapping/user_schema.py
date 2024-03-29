from app.models.User import User
from marshmallow import validate, fields, Schema, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only = True)
    name = fields.String(required=True)
    dni = fields.String(required=True)
    
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)