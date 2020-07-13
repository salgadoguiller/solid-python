from marshmallow import Schema, fields


class UserSchema(Schema):
    profile_id = fields.Str(required=True)
    data_from = fields.Str(required=False, default="request")

    class Meta:
        strict = True