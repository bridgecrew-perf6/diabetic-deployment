# importing the lib
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/images')
def images():
    return "this is the image page"


# contact

# aboutus

app.run() # should be always at the end


"""
http: hyper text transfer protocol
127.0.0.1 - ip address - localhost
:5000 - port
/ - route

http://127.0.0.1:5000/

"""
