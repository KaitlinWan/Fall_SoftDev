#Kaitlin Wan
#SoftDev1 pd6
#K #26: REST STUFF
#T 2018-11-16

from flask import Flask,request,render_template,session,url_for,redirect
import json,urllib.request
from random import randint

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!


@app.route('/')
def hello():
    x = urllib.request.urlopen('https://random.dog/woof.json')
    x = x.read()
    #print(x)
    p = json.loads(x)
    #print(p)
    #print("=======")
    #print(p.keys())
    new = 'https://aws.random.cat/meow'
    y = urllib.request.urlopen(new).read()
    y = json.loads(y)

    l = 'https://api.adviceslip.com/advice'
    z = urllib.request.urlopen(l).read()
    z = json.loads(z)
    z = z['slip']['advice']
    print(z)

    return render_template("template.html", coolpic1 = p['url'], coolpic2 = y['file'], coolpic3 = z)


if __name__ == '__main__':
    app.debug = True
    app.run()
