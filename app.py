import os
from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)


@app.route("/",methods=['GET'])
def Login():
   return render_template('Login.html')


@app.route("/register",methods=['GET'])
def Register():
   return render_template('Register.html')


@app.route("/dashboard",methods=['GET'])
def Dashboard():
   return render_template('Dashboard.html')

# run the application
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5004))
    app.run(debug=True, host='0.0.0.0', port=port)