from flask import Flask, jsonify, request, abort
from flask import Response
import sqlite3
import requests
import hashlib
import json
from flask_cors import CORS
import base64
import datetime
import string
import re

app = Flask(__name__)
CORS(app)
app.config["CORS_SUPPORTS_CREDENTIALS"] = True

def checkUserNameInDb(username):
    connectionState = sqlite3.connect("user_databs.db")
    cursor = connectionState.cursor()
    cursor.execute("SELECT * from User WHERE username = ?",(username,))
    userData = cursor.fetchall()
    connectionState.close()
    if (len(userData) == 0):
        return 1
    return 0

def checkCategoryInDb(categoryname):
     connectionState = sqlite3.connect("user_databs.db")
     cursor = connectionState.cursor()
     cursor.execute("SELECT * from Category WHERE categoryname = ?",(categoryname,))
     categoryData = cursor.fetchall()
     connectionState.close()
     if (len(categoryData) == 0):
        return 1
     return 0

def getcategory(categorydic):
    connectionState = sqlite3.connect("user_databs.db")
    cursor = connectionState.cursor()
    cursor.execute("SELECT * from Category")
    data=cursor.fetchall()
    for i in data:
    	categorydic[i[0]]=i[1]
       
    connectionState.commit()
    connectionState.close()
    return categorydic
    

def checkactid(actid):
	connectionState = sqlite3.connect("user_databs.db")
	cursor = connectionState.cursor()
	cursor.execute("SELECT * from Acts WHERE actId = ?",(actid,))
	actData = cursor.fetchall()
	connectionState.close()
	if len(actData) == 0:
	    return 1
	return 0

def checkusername(user):
	connectionState=sqlite3.connect("user_databs.db")
	cursor=connectionState.cursor()
	cursor.execute("SELECT username FROM User WHERE username=?",(user,))
	userdata=cursor.fetchall()
	connectionState.close()
	if(len(userdata) == 0):
		return 0
	return 1

def checkcategoryname(category):
	connectionState=sqlite3.connect("user_databs.db")
	cursor=connectionState.cursor()
	cursor.execute("SELECT categoryname from Category where categoryname=?",(category,))
	catdata=cursor.fetchall()
	connectionState.close()
	if(len(catdata) == 0):
		return 0
	return 1

def imgB64decode(imgB64):
	try:
		base64.b64encode(base64.b64decode(imgB64)) == imgB64
	except Exception as e:
		return 0
	else:
		return 1

def imgB64decodes(category):
	try:
		connectionState=sqlite3.connect('user_databs.db')
		cursor=connectionState.cursor()
		cursor.execute('SELECT imgB64 from Acts where categoryname=?',(category,))
		img=cursor.fetchall()
		connectionState.close()
		img.decode('base64','strict')
	except Exception as e:
		return 1
	else:
		return 0

def timecheck(timeformat):
	try:
		datetime.datetime.strptime(timeformat, '%d-%m-%Y:%S-%M-%H')
	except:
		return 0
	else:
		return 1

def timechecks(category):
	try:
		connectionState=sqlite3.connect('user_databse.db')
		cursor=connectionState.cursor()
		cursor.execute('SELECT timestamp from Acts where categoryname=?',(category,))
		time=cursor.fetchall()
		connectionState.close()
		datetime.datetime .strptime(time, '%d-%m-%Y')
	except:
		return 0
	else:
		return 1


def checkCategory(category):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * FROM Category where categoryname=?',(category,))
	categorydata=cursor.fetchall()
	connectionState.close()
	if(len(categorydata) == 0):
		return 1
	return 0

def checknoofacts(category):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	cursor.execute("SELECT * FROM Category WHERE categoryname=?",(category,))
	actdata=cursor.fetchall()
	connectionState.close()
	if(len(actdata)<100):
		return 0
	return 1

def checkacts(category,end):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * from Acts where categoryname=?',(category,))
	actno=cursor.fetchall()
	if(len(actno)>=end):
		return 0
	return 1
def checkacts1(category,end):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * FROM Acts where categoryname=?',(category,))
	actno=cursor.fetchall()
	if(len(actno)>=end):
		return 1
	return 0

def checkUserPwd(username,password):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT username,password from Users where username=? and password=?',(username,password,))
	userpwd=cursor.fetchall()
	if(len(userpwd)==0):
		return 1
	return 0

def checkforimg(imgB64):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * from Acts where imgB64=?',(imgB64,))
	imgdata=cursor.fetchall()
	if(len(imgdata)==0):
		return 1
	return 0

def checkforhash(maybe_sha):
	connectionState=sqlite3.connect('user_databs.db')
	cursor=connectionState.cursor()
	if len(maybe_sha) != 40:
		return False
	try:
		sha_int = int(maybe_sha, 16)
	except ValueError:
		return False
	return True

	
	
#1.ADDING USER AND LIST ALL USERS
@app.route("/api/v1/users", methods = ['POST', 'GET' ,'DELETE','PUT'])
def addUser():

	if request.method == "POST":
		user_data = request.get_json()
		#user_data['password'] = (hashlib.sha1(user_data['password'].encode())).hexdigest()
		if checkUserNameInDb(user_data['username']) and checkforhash(user_data['password']) :
			connectionState = sqlite3.connect("user_databs.db")
			cursor = connectionState.cursor()
            #user_data['password'] = (hashlib.sha1(user_data['password'].encode())).hexdigest()
			cursor.execute("INSERT INTO User(username, password) VALUES(?,?)",(user_data['username'], user_data['password']))
			connectionState.commit()
			connectionState.close()
			return jsonify({}), 201
		else:
            #Bad request
			return jsonify({}), 400

        # list all users
	elif request.method == "GET":
		users=[]
		userpass=[]
		dic={}
		connectionState=sqlite3.connect("user_databs.db")
		cursor=connectionState.cursor()
		cursor.execute("SELECT username from User")
		users_data=cursor.fetchall()
		for i in users_data:
			users.append(i[0])
		#for i in users_data:
		#	userpass.append(i)
		#print(userpass)
		#j=0
		#for i in userpass:

		#	print(userpass[j][0])
		#	print(userpass[j][1])
		#	j=j+1
		#r=requests.post(url="http://localhost:8000/api/v1/acts",data=userpass)
		connectionState.commit()
		connectionState.close()
		return jsonify(users),200

	else:
        #method not allowed
		return jsonify({}), 405

        
#2.DELETE USER
@app.route("/api/v1/users/<username>", methods = ['POST', 'GET','DELETE','PUT'])
def removeUser(username):
    if request.method == "DELETE":
    	#if username=="":
    		#return jsonify({}),400
    	if(checkUserNameInDb(username)):
    		return jsonify({}),400
    	else:
            connectionState = sqlite3.connect("user_databs.db")
            cursor = connectionState.cursor()
            cursor.execute("DELETE FROM User where username=?",(username,))   
            '''response = app.response_class(
                status=200,
                mimetype='application/json'
                )
            return response'''
            connectionState.commit()
            connectionState.close()
            return jsonify({}), 200
    else:
        #method not allowed
        return jsonify({}), 405


#@app.route("/api/v1/users/cats/<name>", methods = ['POST', 'GET','DELETE','PUT'])
#def cat(name):
#	r=requests.post('http://localhost:8000/api/v1/categories',data=name)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 1611, debug = True)
