from marshmallow_muffin import Schema, fields


class FooSerializer(Schema):
    _id = fields.Integer()
