from flask import Flask

def runConfig() -> Flask:
    #config flask app name
    app = Flask(__name__)

    #config flask db url connection
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://poli:polieforca@localhost:3306/poli"
    
    #enable hot reload
    app.config['DEBUG'] = True
    
    #config base secret key for hashing
    app.config['SECRET_KEY'] = "random string"

    return app
