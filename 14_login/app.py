#Team KateLin
#Kaitlin Wan + kevin Lin
#SoftDev1 pd6
#K 14: Do I Know You?
#2018-10-01

from flask import Flask,request,render_template,session,url_for,redirect
from util import auth
import os

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "123123123abcabc"


@app.route('/')
def hello():
    if 'user' in session:
        session.pop('user')
    login = ""
    try:
        login = auth.checkInfo(request.args["user"],request.args["pass"])
        print (login)
    except:
        pass
    if login != "Login Successful":
        return render_template('template.html', loginStatus = login)
    else:
        session['user'] = request.args["user"]

        return redirect('/loggedin')

    #Simple HomePage!

@app.route('/loggedin')
def login():
    if 'user' in session:
        dict = request.form
        return render_template('welcome.html', name = session['user'])
    else:
        return render_template('template.html', loginStatus = "You are treading in BAD waters!!")

if __name__ == '__main__':
    app.debug = True
    app.run()
