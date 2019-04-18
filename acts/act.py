from flask import Flask, jsonify, request, abort
from flask import Response
import requests
import sqlite3
#import make_response
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
    connectionState = sqlite3.connect("acts_databs.db")
    cursor = connectionState.cursor()
    cursor.execute("SELECT * from User WHERE username = ?",(username,))
    userData = cursor.fetchall()
    connectionState.close()
    if (len(userData) == 0):
        return 1
    return 0

def checkCategoryInDb(categoryname):
     connectionState = sqlite3.connect("acts_databs.db")
     cursor = connectionState.cursor()
     cursor.execute("SELECT * from Category WHERE categoryname = ?",(categoryname,))
     categoryData = cursor.fetchall()
     connectionState.close()
     if (len(categoryData) == 0):
        return 1
     return 0

def getcategory(categorydic):
    connectionState = sqlite3.connect("acts_databs.db")
    cursor = connectionState.cursor()
    cursor.execute("SELECT * from Category")
    data=cursor.fetchall()
    for i in data:
    	categorydic[i[0]]=i[1]
       
    connectionState.commit()
    connectionState.close()
    return categorydic
    

def checkactid(actid):
	connectionState = sqlite3.connect("acts_databs.db")
	cursor = connectionState.cursor()
	cursor.execute("SELECT * from Acts WHERE actId = ?",(actid,))
	actData = cursor.fetchall()
	connectionState.close()
	if len(actData) == 0:
	    return 1
	return 0

def checkusername(user):
	connectionState=sqlite3.connect("acts_databs.db")
	cursor=connectionState.cursor()
	cursor.execute("SELECT username FROM User WHERE username=?",(user,))
	userdata=cursor.fetchall()
	connectionState.close()
	if(len(userdata) == 0):
		return 0
	return 1

def checkcategoryname(category):
	connectionState=sqlite3.connect("acts_databs.db")
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
		connectionState=sqlite3.connect('acts_databs.db')
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
		connectionState=sqlite3.connect('acts_databse.db')
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
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * FROM Category where categoryname=?',(category,))
	categorydata=cursor.fetchall()
	connectionState.close()
	if(len(categorydata) == 0):
		return 1
	return 0

def checknoofacts(category):
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	cursor.execute("SELECT * FROM Category WHERE categoryname=?",(category,))
	actdata=cursor.fetchall()
	connectionState.close()
	if(len(actdata)<100):
		return 0
	return 1

def checkacts(category,end):
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * from Acts where categoryname=?',(category,))
	actno=cursor.fetchall()
	if(len(actno)>=end):
		return 0
	return 1
def checkacts1(category,end):
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * FROM Acts where categoryname=?',(category,))
	actno=cursor.fetchall()
	if(len(actno)>=end):
		return 1
	return 0

def checkUserPwd(username,password):
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT username,password from Users where username=? and password=?',(username,password,))
	userpwd=cursor.fetchall()
	if(len(userpwd)==0):
		return 1
	return 0

def checkforimg(imgB64):
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	cursor.execute('SELECT * from Acts where imgB64=?',(imgB64,))
	imgdata=cursor.fetchall()
	if(len(imgdata)==0):
		return 1
	return 0

def checkforhash(maybe_sha):
	connectionState=sqlite3.connect('acts_databs.db')
	cursor=connectionState.cursor()
	if len(maybe_sha) != 40:
		return False
	try:
		sha_int = int(maybe_sha, 16)
	except ValueError:
		return False
	return True
	
	


#3,4.ADD CATEGORY AND LIST CATEGORY
    
@app.route("/api/v1/categories", methods = ['POST', 'GET','DELETE','PUT'])
def addcategory():
	if request.method == "GET":
		categories = {}
		getcategory(categories)
		if len(categories):
			#print(categories)
			return jsonify(categories),200
			
		else:
			return jsonify({}),204               
	elif request.method == "POST":
		category_data = request.get_json()
		#print(category_data)
		#cat_data=[]
		#cat_data.append(str(category_data['categoryname']))
		numberofacts=0
		#print(cat_data)
		if category_data[0]=="":
			return jsonify({}),400
		if checkCategoryInDb(category_data[0]):
			connectionState = sqlite3.connect("acts_databs.db")
			cursor = connectionState.cursor()
			#category_data['numberofacts']=0
			cursor.execute("INSERT INTO Category(categoryname, numberofacts) VALUES(?, ?)", (category_data[0],numberofacts,))
			connectionState.commit()
			connectionState.close()
			return jsonify({}), 201
		else:
            #Bad request
			return jsonify({}), 400
	else:       
        #Method not allowed
		return jsonify({}), 405


#5.REMOVE CATEGORY
@app.route("/api/v1/categories/<categoryname>", methods = ['POST', 'GET', 'DELETE', 'PUT'])
def removeCategory(categoryname):
    if request.method == 'DELETE':
    	
    	if checkCategoryInDb(categoryname):
    		return jsonify({}), 400
    	else:
            connectionState = sqlite3.connect("acts_databs.db")
            cursor = connectionState.cursor()
            cursor.execute("DELETE FROM Category where categoryname IS ?",(categoryname,)) 
            cursor.execute("DELETE FROM Acts where categoryname is ?",(categoryname,))
            connectionState.commit()
            connectionState.close()
            return jsonify({}), 200
    else:
        #method not allowed
        return jsonify({}), 405


#6.LIST ACTS FOR A GIVEN CATEGORY
@app.route('/api/v1/categories/<category>/acts' , methods=['GET','POST','DELETE','PUT'])
def actsforcategory(category):
	#print("ACTS FOR CATEGORIES")
	#print("ARGS ", request.args)
	start = request.args.get("start")
	end = request.args.get("end")
	#if start:
	#	print("START: ", start, "END: ", end)
	if start==None and end==None:
		print("ACTS FOR CATEGORIES")
		if request.method=='GET':
			
			mydic={}
			actlist=[]
			if checkCategory(category): #or checkUserNameInDb(category): #or imgB64decodes(category) or timechecks(category):
				return jsonify({}),204
			elif checknoofacts(category):
				return jsonify({}),413
			else:
				connectionState=sqlite3.connect('acts_databs.db')
				cursor=connectionState.cursor()
				#r=requests.get(url="http://localhost:5656/api/v1/users")
				#user=r.json()
				#cursor.execute("INSERT INTO User(username,password) VALUES (?,NULL)",(user,))
				#for i in user:
				#	print(i)
				cursor.execute('SELECT actId,username,timestamp,caption,imgB64,upvotes from Acts where categoryname=?',(category,))
				act=cursor.fetchall()	
				j=len(act)
				for k in act:
					mydic={"actId":k[0],"Username":k[1],"timestamp":k[2],"Caption":k[3],"imgB64":k[4],"Upvotes":k[5]}
					#return ({'actId':k[0],'Username':k[1],'timestamp':k[2],'Caption':k[3],'imgB64':k[4],'Upvotes':k[5]}),200
					actlist.append(mydic)
					#finaldic.update(mydic)	
				return jsonify(actlist),200

				#return jsonify(mydic),200
					#return jsonify(k[0]),200
				
				connectionState.commit()	
				connectionState.close()
		else:
			return jsonify({}),405
	elif start!= None and end==None:
		return jsonify({}),204
	elif start==None and end!=None:
		return jsonify({}),204
	elif start!=None and end!=None:
		value=categoryrange(category,start,end)
		return value



#7.LIST NUMBER OF ACTS FOR A CATEGORY
  
@app.route('/api/v1/categories/<category>/acts/size' ,methods=['GET','PUT','POST','DELETE'])
def acts(category):
	if request.method =='GET':
		
		if checkCategory(category):
			return jsonify({}),204
		else:
			connectionState=sqlite3.connect("acts_databs.db")
			cursor=connectionState.cursor()
			cursor.execute('SELECT numberofacts FROM Category WHERE categoryname=?',(category,))
			data=cursor.fetchall()
			print(data)	
			return jsonify(data[0]),200

	else:
		return jsonify({}),405


#8. LIST ACTS FOR A GIVEN CATEGORY WITHIN A RANGE
#@app.route('/api/v1/categories/<category>/acts?start=<int:start>&end=<int:end>' , methods=['GET','POST','DELETE','PUT'])
#app.route('/api/v1/categories/<category>/acts?start=<int:start>/<int:end>' , methods=['GET','POST','DELETE','PUT'])
def categoryrange(category,start,end):
	print("TESTTTTTTT")
	#print("REQUEST ", request.method)
	if request.method=='GET':
		if category=="":
			return jsonify({}),400
		mydic={}
		actrangelist=[]
		diff = int(end)-int(start)+1
		#print("diff ",diff)
		#	print(diff)
		if checkCategory(category):
			#print("WRONG CATEGORY")
			return jsonify({}),204	
		if diff > 100:
			print("Difference greater than 100")
			return jsonify({}),413
		elif int(start) < 1 or checkacts(category,int(end)):
			#print("WRECKED")
			return jsonify({}),204
		elif  int(start)>=1 and checkacts1(category,int(end)):
			#print("HELLO WORLD")
			connectionState=sqlite3.connect('acts_databs.db')
			cursor=connectionState.cursor()
			cursor.execute('SELECT actId,username,timestamp,caption,imgB64,upvotes from Acts where categoryname=? order by date(timestamp) DESC limit ? offset ? ',(category,diff,int(start)-1,))
			actdesc=cursor.fetchall()
			j=len(actdesc)
			for k in actdesc:
				mydic={"actId":k[0],"Username":k[1],"timestamp":k[2],"Caption":k[3],"imgB64":k[4],"Upvotes":k[5]}
				actrangelist.append(mydic)
				print("HERE1")

			print(actrangelist)
			return jsonify(actrangelist),200
			connectionState.commit()
			connectionState.close()
	else:
		return jsonify({}),405


#9. UPVOTE AN ACT

@app.route('/api/v1/acts/upvote' , methods=['GET','POST','DELETE','PUT'])
def upvote():
	if request.method =='POST':
		upvote_data=request.get_json();
		if checkactid(upvote_data[0]):
			return jsonify({}),400
		else:
			connectionState=sqlite3.connect('acts_databs.db')
			cursor=connectionState.cursor()
			cursor.execute('UPDATE Acts SET upvotes=upvotes+1 WHERE actId=?',(upvote_data[0	],))
			connectionState.commit()
			connectionState.close()
			return jsonify({}),200
	else:
		jsonify({}),405


#10.REMOVE AN ACT

@app.route('/api/v1/acts/<actid>' ,methods=['GET','POST','DELETE','PUT'])
def removeact(actid):
	if request.method == 'DELETE':
		print("1")
		if checkactid(int(actid)):
			return jsonify({}),400
		else:
			connectionState=sqlite3.connect('acts_databs.db')
			cursor=connectionState.cursor()
			cursor.execute('UPDATE Category SET numberofacts=numberofacts-1 WHERE categoryname=(SELECT categoryname from Acts WHERE actId IS ?)',(int(actid),))
			cursor.execute('DELETE FROM Acts WHERE actId IS ?',(int(actid),))
			connectionState.commit()
			connectionState.close()	

			return jsonify({}),200
	else:
		jsonify({}),405




#11. UPLOAD AN ACT

@app.route('/api/v1/acts' , methods=['GET','POST','DELETE','PUT'])
def upload():
	if request.method == 'POST':
		currtime=datetime.datetime.now()
		act_data=request.get_json()
		#print("Hello")
		connectionState=sqlite3.connect('acts_databs.db')
		cursor = connectionState.cursor()
		r=requests.get(url="http://18.204.92.74:8080/api/v1/users")
		users=r.json()
		print(users)
		#for i in users:
		#	if i==
		#j=0
		#for i in users:
		#	usernm=users[j][0]
		#	print(usernm)
		#	passwrd=users[j][1]
		#	print(passwrd)
		#	j=j+1
		#cursor.execute("INSERT INTO User(username,password) VALUES (?,?)",(usernm,passwrd))
		#cursor.execute("SELECT username from User")
		#user=cursor.fetchall()
		for i in users:
			if(i==act_data['username']):
				if checkactid(act_data['actId']) and checkcategoryname(act_data['categoryName']) and timecheck(act_data['timestamp']) and imgB64decode(act_data['imgB64']):
					act_data['upvotes']=0
					cursor.execute('INSERT INTO Acts(categoryname,actId,username,timestamp,caption,imgB64,upvotes) VALUES (?,?,?,?,?,?,?)', \
		          	(act_data['categoryName'],act_data['actId'],act_data['username'],act_data['timestamp'],act_data['caption'],act_data['imgB64'],act_data['upvotes']))
					cursor.execute('UPDATE Category SET numberofacts=numberofacts+1 WHERE categoryname=?',(act_data['categoryName'],))
					connectionState.commit()
					connectionState.close()
					return jsonify({}),201

				else:
					return jsonify({}),400
			else:
				continue;
	else:
		return jsonify({}),405

#Route for generating act id

@app.route('/api/v1/actid' , methods=['GET','POST','DELETE','PUT'])
def getactid():
	if request.method=='GET':
		connectionState=sqlite3.connect('acts_databs.db')
		cursor = connectionState.cursor()
		cursor.execute('SELECT actId from Acts order by actId')
		aid=cursor.fetchall()
		if len(aid)==0:
			actId=0
		else:
			cursor.execute('Select MAX(actId) from Acts')
			maxid=cursor.fetchall()
			print(maxid[0][0])
			actId=maxid[0][0]+1
		return jsonify([actId]),201
	else:
		return jsonify({}),405


#LOGIN
@app.route('/api/v1/login' , methods=['GET','POST','DELETE','PUT'])
def login():
	if request.method=='POST':
		user_datalogin = request.get_json()
		connectionState=sqlite3.connect('acts_databs.db')
		cursor=connectionState.cursor()
		user_data['password'] = (hashlib.sha1(user_data['password'].encode())).hexdigest()
		if checkNamePwd(user_datalogin['username'],user_datalogin['password']):
			return jsonify({"WRONG CREDENTIALS"}),400
		else:
			return jsonify({}),200
	else:
		return jsonify({}),405


#To get actid using imgB64
@app.route('/api/v1/img' , methods=['GET','POST','DELETE','PUT'])
def imgactid():
	if request.method=='GET':
		img_data=request.get_json()
		if checkforimg(img_data['imgB64']):
			return jsonify({}),400
		else:
			connectionState=sqlite3.connect('acts_databs.db')
			cursor=connectionState.cursor()
			cursor.execute('SELECT actId from Acts where imgB64=?',(img_data['imgB64'],))
			idact=cursor.fetchall()
			connectionState.commit()
			connectionState.close()
			return jsonify([idact]),200
	else:
		return jsonify({}),405





if __name__ == '__main__':
    app.run(host='0.0.0.0',port =1611, debug = True)
