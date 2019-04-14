from flask import Flask,redirect,render_template,request,session,abort,jsonify,make_response
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy
from base64 import b64encode, b64decode
from datetime import datetime
import string
import requests
import os
import json
import hashlib
import binascii

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "users.db"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

class Reg(db.Model):
    username = db.Column(db.String(80), unique = True, nullable=False, primary_key=True)
    password = db.Column(db.String(40), nullable=False)

@app.route("/")
def home():
	return "USER CONTAINER"

#API 1
@app.route("/api/v1/users", methods=['POST', 'GET'])
def adduser():
	print(request.method)
        if request.method=='GET':
		data = request.get_json()
                print("GET")
		userlist = Reg.query.all()
		if len(userlist)==0:
			return make_response(json.dumps([]), 204)
		res = [detail.username for detail in userlist]
                print("got list")
		return make_response(json.dumps(res), 200)

	if request.method=='POST':
		data = request.get_json()
		us = data['username']
		temp = Reg.query.filter_by(username=us).first()
		if temp is not None:
			return make_response(jsonify({}), 400)
		pa = data['password']
		if len(pa)!=40 or not int(pa, 16) or type(pa)!=str:
			return make_response(jsonify({}), 400)
		temp = Reg(username=us, password=pa)
		db.session.add(temp)
		db.session.commit()
		return make_response(jsonify({}), 201)
	else:
		return make_response(jsonify({}), 405)

#API 2
@app.route("/api/v1/users/<username>", methods=['DELETE','GET'])
def removeuser(username):
	print("its here")
        data = request.get_json()
	if request.method=='DELETE':
		temp = Reg.query.filter_by(username = username).first()
		if temp is None:
			return make_response(jsonify({}),400)
		else:
			db.session.delete(temp)
			db.session.commit()
			return make_response(jsonify({}),200)
	else:
		return make_response(jsonify({}), 405)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=80)
