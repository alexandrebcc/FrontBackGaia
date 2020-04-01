# coding:utf-8
from datetime import datetime
#from app import db
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db

class Instituicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    sobrenome = db.Column(db.String(255))
    cidade = db.Column(db.String(255))
    estado = db.Column(db.String(255))
    cep = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    endereco = db.Column(db.String(255))
    endereco2 = db.Column(db.String(255))
    validade = db.Column(db.String(255))
    descricao = db.Column(db.String(1000))
    midia = db.Column(db.String(1000))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)






















'''class Instituicoes(db.Model):
    __tablename__ = instituicoes
    id = db.Column(db.Integer, primary_key = True)
    nome  = db.Column(db.String(80))
    sobrenome  = db.Column(db.String(80))
    cidade  = db.Column(db.String(80))
    estado  = db.Column(db.String(80))
    cep  = db.Column(db.String(80))
    email = db.Column(db.String(80))
    endereco1 = db.Column(db.String(80))
    endereco2 = db.Column(db.String(80))
    telefone = db.Column(db.String(80))
    descricao = db.Column(db.String(80))
    midia = db.Column(db.String(80))
    dadosBancarios = db.Column(db.String(80))
    data_criacao = db.Column(db.DateTime)
    
    login_id = db.column(db.Integer,db.ForeignKey('login.id'))
    login=db.relationship('Login', foreign_Keys=login_id)

      

    def __init__(self, nome,sobrenome,cidade,estado,cep,email, endereco1,endereco2,
                telefone,descricao,midia,dadosBancarios,login,senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.email = email
        self.endereco1 = endereco1
        self.endereco2 = endereco2
        self.telefone = telefone  
        self.descricao = descricao
        self.midia = midia
        self.dadosBancarios = dadosBancarios
        self.login = login
        self.senha = senha 
        self.data_criacao = datetime.now()


class Login(db.model):
    __tablename__= login
    id = db.column(db.Integer, primary_key = True)
    username = db.column(db.string(80), unique=True)
    login = db.Column(db.String(80))
    senha = db.Column(db.String(80))
    nome = db.column(db.string(80))
    email = db.column(db.string(80),unique = True)
    
    

    def __init__(self, username,login,senha,nome,email):
        self.username = username
        self.login = login
        self.senha = senha
        self.nome = nome
        self.email = email
'''