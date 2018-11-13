#Team KateLin
#Kaitlin Wan + Kevin Lin
#SoftDev1 pd6
#K 14: Do I Know You?
#2018-10-01

from flask import Flask,request,render_template,session,url_for,redirect
import json,urllib.request

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!


@app.route('/')
def hello():
    with urlib.request(https://api.nasa.gov/planetary/apod?api_key=SFVhYXCLPaL8AiaRP6JfTlcPSCF6c90qCF3cLQiA)
    https://api.nasa.gov/planetary/apod?api_key=SFVhYXCLPaL8AiaRP6JfTlcPSCF6c90qCF3cLQiA
    return render_template("template.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
