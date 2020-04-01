from app import db
from app.models import instituicoes

def drop_db():
    db.drop_all()

def create_db():
    db.create_all()
    print("Banco criado.")

def populate_db():
    # Insere uma nota no banco
    instituicao = instituicoes('casa do bem','do bem','aracati','ce','62800-000','shdjsh@gmial.com','fenda1','fenda do bequini2','887878878',
    'onsdoasoda asdasdla jsdakjdsla jsdkajldsj jdal','hsdjhaksdhkahsdkahsdka','bsdashdja, dahsdkahsm, djhajhds, sdjas','fenda','fenda')
    db.session.add(instituicao)
    db.session.commit()

    # Insere uma nota no banco
    instituicao = instituicoes('casa xand','do bem','aracati','ce','62800-000','sasdasddjsh@gmial.com','nda1','nda do bequini2','8sds78878',
    'onsdoasoda asdassdsddla sdsaa dssas jdal','hsdjhaksdhkajsdhahsdkahhsdkahsdka','asdas, dahasdsd sdsdas, sdjas','dois','dois')
    db.session.add(instituicao)
    db.session.commit()
    # Atualiza uma nota
    instituicao.nome = 'atualizado'
    db.session.commit()

    # Atualiza uma nota
    nota = instituicoes.query.all()[0]
    db.session.delete(nota)
    db.session.commit()

    # Obtém todas as notas
    instituicao = instituicoes.query.all()
    for inst in instituicao:
        print('nome:', inst.nome)

    # Filtrando informações
    '''
    notas = Nota.query.filter_by(titulo='Estudar Flask-SqlAlchemy').all()
    print(notas[0].titulo)

    notas = Nota.query.filter_by(titulo='...').all()
    print(notas)'''
    