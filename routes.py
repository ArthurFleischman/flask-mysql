from flask import Flask, request, Response, jsonify
from model import User, db
from sqlalchemy import delete

def registerRoutes(app: Flask):
    
    @app.post("/user")
    def insertUser():
        try:
            raw_data = request.json
            print(raw_data)
            user = User(raw_data["name"], raw_data["password"], raw_data["email"])
            db.session.add(user)
            db.session.commit()
            return ("user inserted", 200)
        except:
            return ("could not insert user", 500)

    @app.get("/users")
    def getUsers() -> list:
        # user_list = [users.to_json() for users in User.query.all()]
        user_list = list(map(User.to_json, User.query.all()))
        return jsonify(user_list)

    @app.get("/user/<uid>")
    def getUser(uid):
        try:
            return User.query.filter_by(id=uid).first().to_json()
        except:
            return (f"user id = {uid} not found", 404)

    @app.delete("/user/<uid>")
    def deleteUSer(uid):
        try:
            User.delete().where(id==uid)
            return ("user deleted successfully", 200)
        except:
            return ("user id not found", 404)

    @app.get("/ping")
    def ping():
        return "pong", 200  