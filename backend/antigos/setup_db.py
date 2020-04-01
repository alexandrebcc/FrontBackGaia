# coding:utf-8
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models import instituicoes

if __name__ == '__main__':
    
    # cria o banco
    db.create_all()

    # Insere uma nota no banco
    instituicao = instituicoes('Bob Esponja', 'Fenda do biquini','8899858585','bob@gmail.com','trabaha para o sirigueijo','sj','bb','bobesponha','bobesponja')
    db.session.add(instituicao)
    db.session.commit()

    # Atualiza uma nota
    instituicao.nome = 'Estudar Flask-SqlAlchemy'
    db.session.commit()

    # Atualiza uma nota
    instituicao = Nota.query.all()[0]
    db.session.delete(nota)
    db.session.commit()

    # Obtém todas as notas
    instituicao = instituicoes.query.all()
    for nome in instituicao:
        print(nome.nome)
'''
    # Filtrando informações
    notas = Nota.query.filter_by(titulo='Estudar Flask-SqlAlchemy').all()
    print(notas[0].titulo)

    notas = Nota.query.filter_by(titulo='...').all()
    print(notas)
    '''