from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200)) 

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def to_json(self):
        return {"id": self.id, "name":self.name,"email":self.email}
