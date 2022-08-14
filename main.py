from flask import Flask, request
from config import runConfig
from model import db
from routes import registerRoutes

def main():
    app = runConfig()
    db.init_app(app)
    registerRoutes(app)
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()


