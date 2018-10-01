#Kaitlin Wan + kevin Lin
#SoftDev1 pd6
#K 14: Do I Know You?
#2018-10-01

from flask import Flask,request,render_template,session,url_for,redirect
from util import auth

app = Flask(__name__)

@app.route('/')
def hello():
    login = "Test"
    try:
        login = checkInfo(request.args["user"],request.args["pass"])
    except:
        pass
    return render_template('template.html', loginStatus = login)
    #Simple HomePage!

if __name__ == '__main__':
    app.debug = True
    app.run()
