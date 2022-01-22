import os
from urllib import request
from flask import Flask ,redirect,url_for,request
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def Login():
   if request.method=='POST':
       print("Login")
       return render_template('Login.html')
   else:    
         return render_template('Login.html')






@app.route('/register',methods=['GET','POST'])
def Register():
   if request.method=='POST':
       return render_template('Register.html')
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