import os
from urllib import request
from flask import Flask ,redirect,url_for,request
from flask import render_template
import pymongo
# creates a Flask application, named app
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["users"]
mycol = mydb["userdetails"]

@app.route('/login',methods=['POST','GET'])
def Login():
   if request.method=='POST' and 'username' in request.form and 'password' in request.form:
       username=request.form['username']
       password=request.form['password']
       myquery={'username': username,'password':password }
       if (mycol.find(myquery)):
           f=0
           for x in mycol.find(myquery):
               f+=1
           if f>0:    
               return render_template('Dashboard.html',msg=["logged in successfully",username])
       print("Login")
       return render_template('Register.html',msg="username not exist please register")
   else:    
         return render_template('Login.html')






@app.route('/register',methods=['GET','POST'])
def Register():
   if request.method=='POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
       username=request.form['username']
       password=request.form['password']
       email=request.form['email']
       myquery={'username': username}
       if (mycol.find(myquery)):
           f=0
           for x in mycol.find(myquery):
               f+=1
           if f>0:    
               return render_template('Register.html',msg="Username already exist")
       
       mydict = { "username": username, "password": password ,"email" :email}
       mycol.insert_one(mydict)

       return render_template('Login.html',msg="Registered successfully")    
      
   else:    
         return render_template('Register.html')




@app.route('/dashboard',methods=['GET','POST'])
def Dashboard():
   if request.method=='POST':
       return render_template('Login.html')
   else:    
         return render_template('Dashboard.html')



# run the application
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5004))
    app.run(debug=True, host='0.0.0.0', port=port)