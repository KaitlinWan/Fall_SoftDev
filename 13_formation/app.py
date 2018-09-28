#Kaitlin Wan
#SoftDev1 pd6
#K #08: Fill Yer Flask
#2018-09-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('template.html')
    #Simple HomePage!

if __name__ == '__main__':
    app.debug = True
    app.run()
