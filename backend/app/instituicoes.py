from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from .model import Instituicao
from .serealizer import InstituicaoSchema


bp_instituicao = Blueprint('instituicao', __name__)


@bp_instituicao.route('/instituicoes', methods=['GET'])
#@jwt_required
def mostrar():
    result = Instituicao.query.all()
    return InstituicaoSchema(many=True).jsonify(result), 200


@bp_instituicao.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Instituicao.query.filter(Instituicao.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_instituicao.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = InstituicaoSchema()
    query = Instituicao.query.filter(Instituicao.id == identificador)
    import ipdb; ipdb.set_trace()
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

@bp_instituicao.route('/cadastrar', methods=['POST'])
def cadastrar():
    
    
    bs = InstituicaoSchema()
    dados = bs.load(request.json)
    
    #import ipdb; ipdb.set_trace() bara debugar
    
    current_app.db.session.add(dados)
    current_app.db.session.commit()
    return bs.jsonify(dados), 201
    
