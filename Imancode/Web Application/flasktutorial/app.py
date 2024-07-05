# flask is a module
# inside this module we have a class called Flask
# Let us import the class "Flask"

from flask import Flask

# let us create an instance of object of the class Flask
# "Flask" class has __init__ (constructor) method
# The constuctor takes file which is going to be the main program
# as parameter
# In other words, we are saying app.py is the main program
# to Flask name
app = Flask(__name__)

# if anybody make a http request for "/" then execute
# the following function
# which return Hello 


@app.route("/")
def say_hello():
    return "Hello World!!!"