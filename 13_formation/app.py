#Kaitlin Wan
#SoftDev1 pd6
#K #13: Echo Echo Echo . . .
#2018-09-28

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('template.html',fmeth=request.method)
    #Simple HomePage!

@app.route('/auth',methods = ["POST"])
def authenticate():
    dict = request.form
    return render_template('template0.html',name=dict["user"],fmethod=request.method)

if __name__ == '__main__':
    app.debug = True
    app.run()
