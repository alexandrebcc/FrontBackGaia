from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Instituicao, User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class InstituicaoSchema(ma.ModelSchema):
    class Meta:
        model = Instituicao

    nome = fields.Str(required=True)
    sobrenome = fields.Str(required=True)
    cidade = fields.Str(required=True)
    estado = fields.Str(required=True)
    cep = fields.Str(required=True)
    email = fields.Str(required=True)
    senha = fields.Str(required=True)
    endereco = fields.Str(required=True)
    endereco2 = fields.Str(required=True)
    validade = fields.Str(required=True)
    descricao = fields.Str(required=True)
    midia = fields.Str(required=True)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não envie pelo amor de deus o ID')

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
