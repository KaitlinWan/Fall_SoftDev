#Kaitlin Wan
#SoftDev1 pd6
#K #08: Fill Yer Flask
#2018-09-19

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!! WELCOME TO MY FLASK APP!"
    #Simple HomePage!

@app.route('/<name>')
def hello_name(name): #personalize
    return "Hello {}! Wonderful name you have there!".format(name)

@app.route('/<name>/<age>')
def personal(name,age):
    s = "Hello {}!".format(name)
    s += " I am {}!".format(age)
    #How do I go to the next line? \n doesn not work?
    s += "In 5 years, you will be..."
    pi = int(age) + 5
    s += str(pi)
    return s

if __name__ == '__main__':
    app.debug = True
    app.run()
