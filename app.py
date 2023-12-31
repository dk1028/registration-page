from flask import Flask, render_template, request, redirect 
from models import db
import os
from models import Fcuser
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, user!"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        userid = request.form.get('userid') 
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        print(password) 

        if not (userid and username and password and re_password) :
            return "Write all info"
        elif password != re_password:
            return "Verify your password"
        else: 
            fcuser = Fcuser()         
            fcuser.password = password           
            fcuser.userid = userid
            fcuser.username = username      
            db.session.add(fcuser)
            db.session.commit()
            return "Successfully registered"

        return redirect('/')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))  
    dbfile = os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True     
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

    db.init_app(app) 
    db.app = app
    db.create_all()  


    app.run(host='127.0.0.1', port=5000, debug=True) 