from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .model import configure as config_db
from .serealizer import configure as config_ma
#from app import services
#from app import routes
#from app import model


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['FLASK_APP']=app
    app.config['FLASK_ENV']= "Development"
    app.config['FLASK_DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'Batatinhas voadoras são melhores que eu'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    JWTManager(app)

    from .instituicoes import bp_instituicao
    app.register_blueprint(bp_instituicao)

    from .user import bp_user
    app.register_blueprint(bp_user)

    #from .login import bp_login
    #app.register_blueprint(bp_login)

    return app





